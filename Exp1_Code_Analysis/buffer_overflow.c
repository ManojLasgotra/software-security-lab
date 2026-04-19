#include <stdio.h>
#include <string.h>

// ----------- VULNERABLE CODE -----------
void vulnerable() {
    char buffer[10];
    printf("Enter input (Vulnerable): ");
    gets(buffer);  // ❌ unsafe (buffer overflow)
    printf("You entered: %s\n", buffer);
}

// ----------- FIXED CODE -----------
void secure() {
    char buffer[10];
    printf("Enter input (Secure): ");
    fgets(buffer, sizeof(buffer), stdin);  // ✅ safe
    printf("You entered: %s\n", buffer);
}

int main() {
    vulnerable();
    secure();
    return 0;
}
