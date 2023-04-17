#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 256

// Function to check if a command exists on the system
int command_exists(char *command) {
    return system(command) == 0;
}

// Function to install Python and pip depending on the distribution
void install_dependencies() {
    char distro[BUFFER_SIZE];
    FILE *fp = fopen("/etc/os-release", "r");

    // Read the contents of /etc/os-release to determine the distribution
    while (fgets(distro, BUFFER_SIZE, fp) != NULL) {
        if (strstr(distro, "ID=") != NULL) {
            // Remove the "ID=" prefix and newline characters
            char *distro_name = strtok(distro, "=");
            distro_name = strtok(NULL, "\n");

            // Install Python and pip using the appropriate package manager
            if (strcmp(distro_name, "ubuntu") == 0 || strcmp(distro_name, "debian") == 0) {
                if (!command_exists("python3")) {
                    system("sudo apt-get update");
                    system("sudo apt-get install -y python3");
                }
                if (!command_exists("pip3")) {
                    system("sudo apt-get install -y python3-pip");
                }
            } else if (strcmp(distro_name, "arch") == 0) {
                if (!command_exists("python")) {
                    system("sudo pacman -Sy --noconfirm python");
                }
                if (!command_exists("pip")) {
                    system("sudo pacman -Sy --noconfirm python-pip");
                }
            } else if (strcmp(distro_name, "fedora") == 0 || strcmp(distro_name, "centos") == 0) {
                if (!command_exists("python3")) {
                    system("sudo dnf install -y python3");
                }
                if (!command_exists("pip3")) {
                    system("sudo dnf install -y python3-pip");
                }
            } else {
                printf("Unsupported distribution: %s\n", distro_name);
                exit(1);
            }
            break;
        }
    }
    fclose(fp);
}

int main() {
    // Install Python and pip if necessary
    if (!command_exists("python3") || !command_exists("pip3")) {
        install_dependencies();
    }

    // Check if requirements.txt exists
    if (access("requirements.txt", F_OK) == -1) {
        printf("requirements.txt not found in the current directory.\n");
        exit(1);
    }

    // Open requirements.txt and parse the package names
    FILE *fp = fopen("requirements.txt", "r");
    char package_name[BUFFER_SIZE];

    while (fscanf(fp, "%s", package_name) != EOF) {
        // Install the package using pip
        char pip_command[BUFFER_SIZE];
        snprintf(pip_command, BUFFER_SIZE, "pip3 install %s", package_name);
        int return_value = system(pip_command);

        if (return_value != 0) {
            printf("Failed to install %s.\n", package_name);
        }
    }

    fclose(fp);
    return 0;
}

