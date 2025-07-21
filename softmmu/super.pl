#!/usr/bin/perl
use Socket;

$port = 9900;
@exec = ("/home/softmmu/ld");

# create socket
socket(SERVER, PF_INET, SOCK_STREAM, 6) or die "socket failed: $!";
setsockopt(SERVER, SOL_SOCKET, SO_REUSEADDR, pack("l", 1)) or die "setsockopt failed: $!";
bind(SERVER, sockaddr_in($port, INADDR_ANY)) or die "bind failed: $!";
listen(SERVER, SOMAXCONN) or die "listen failed: $!";

$SIG{"CHLD"} = "IGNORE";
$| = 1;

print "Listening on port $port...\n";

while ($addr = accept CLIENT, SERVER) {
    $| = 1;
    my ($cport, $packed_ip) = sockaddr_in($addr);
    my $ip = inet_ntoa($packed_ip);
    print "$ip:$cport connected\n";

    my $pid = fork();

    if (!defined $pid) {
        warn "fork failed: $!";
        close CLIENT;
        next;
    }

    if ($pid == 0) {
        # child process
        $| = 1;
        close SERVER;

        open STDIN,  "<&CLIENT" or die "redirect STDIN failed: $!";
        open STDOUT, ">&CLIENT" or die "redirect STDOUT failed: $!";
        open STDERR, ">&CLIENT" or die "redirect STDERR failed: $!";
        close CLIENT;

        exec @exec or die "exec failed: $!";
        exit 0;  # should never reach here
    }

    # parent process
    close CLIENT;
}

close SERVER;
