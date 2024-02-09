#include <stdio.h>

int main() {
    float num1, num2, sum, difference, division, multiplication;
    
    printf("Ingresa el primer numero flotante: ");
    scanf("%f", &num1);
    
    printf("Ingresa el segundo numero flotante: ");
    scanf("%f", &num2);
    
    sum = num1 + num2;
    difference = num1 - num2;
    division = num1 / num2;
    multiplication = num1 * num2;
    
    printf("Suma: %.2f\n", sum);
    printf("Resta: %.2f\n", difference);
    printf("Division: %.2f\n", division);
    printf("Multiplicacion: %.2f\n", multiplication);
    
    return 0;
}
