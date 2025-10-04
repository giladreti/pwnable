# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ida-domain",
# ]
# ///
import ida_domain
from ida_domain import Database
from ida_domain.database import IdaCommandOptions

NOP_FUNC_PREFIX = bytes.fromhex("55 48 89 E5")
NOP_FUNC_SUFFIX = bytes.fromhex("5D C3")

with Database.open("pwnsandbox.i64", IdaCommandOptions(auto_analysis=True), save_on_close=True) as db:
    for func in db.functions:
        print(f"Function: {func.name}, Address: {hex(func.start_ea)}")
        bytes_ = db.bytes.get_bytes_at(func.start_ea, func.size())
        print(f"  First 7 bytes: {bytes_[:10].hex(' ')}")
        if bytes_ == NOP_FUNC_PREFIX + b"\x90" * (func.size() - len(NOP_FUNC_PREFIX) - len(NOP_FUNC_SUFFIX)) + NOP_FUNC_SUFFIX:
            print(f"  NOP function detected at {hex(func.start_ea)}")
            db.functions.set_name(func, f"nop_{func.start_ea:x}")
            print(f"  Renamed to nop_{func.start_ea:x}")
        else:
            try:
                pseudocode = "\n".join(db.functions.get_pseudocode(func))
            except RuntimeError as e:
                continue

            if all(x in pseudocode for x in ["read(0, buf, 0x10u)", "puts(buf)", "char buf[24]"]):
                print(f"  read_and_puts function detected at {hex(func.start_ea)}")
                db.functions.set_name(func, f"read_and_puts_{func.start_ea:x}")
                print(f"  Renamed to read_and_puts_{func.start_ea:x}")

            if all(x in pseudocode for x in ["(0x40u)", "puts(s)"]):
                print(f"  read_bytes_and_puts function detected at {hex(func.start_ea)}")
                db.functions.set_name(func, f"read_bytes_and_puts_{func.start_ea:x}")
                print(f"  Renamed to read_bytes_and_puts_{func.start_ea:x}")