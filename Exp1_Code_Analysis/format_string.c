#include <stdio.h>

// ----------- VULNERABLE CODE -----------
void vulnerable() {
    char input[100];
    printf("Enter input (Vulnerable): ");
    gets(input);
    printf(input);  // ❌ dangerous
}

// ----------- FIXED CODE -----------
void secure() {
    char input[100];
    printf("Enter input (Secure): ");
    fgets(input, sizeof(input), stdin);
    printf("%s", input);  // ✅ safe
}

int main() {
    vulnerable();
    secure();
    return 0;
}
