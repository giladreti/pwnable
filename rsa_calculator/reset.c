// manually start challenge when its down
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <errno.h>

int is_port_open(int port) {
    int sockfd;
    struct sockaddr_in addr;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) return 0;

    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    int result = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    close(sockfd);
    return (result == 0);
}

int main() {
    int port = 9012;

    if (is_port_open(port)) {
        printf("Service is already running on port %d.\n", port);
        return 0;
    }

    printf("Port %d is not open. Attempting restart...\n", port);

    if (setreuid(0, 0) != 0) {
        perror("setreuid failed");
        return 1;
    }

    int ret = system("/home/rsa_calculator_pwn/run.sh");
    if (ret != 0) {
        fprintf(stderr, "Failed to restart service (code %d)\n", ret);
        return 1;
    }

    printf("Service back online\n");
    return 0;
}

