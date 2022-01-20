#define stdout 1

#define FILENAME "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"

int main() {
    char flag[256];
    int fd = open(FILENAME, 0, O_RDONLY);
    ssize_t len = read(fd, flag, 256);
    write(stdout, flag, len);
    return 0;
}