//
//  main.c
//  Pre Load
//
//  Created by Hugo Ayre on 3/17/17.
//  Copyright © 2017 Pre Load. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    float price , standards, result;
    
    printf("Enter the price: ");
    scanf("%f", &price);
    
    printf("Enter the number of standard drinks: ");
    scanf("%f", &standards);
    
    result = standards/price;
    
    
    printf("You are getting %f standard drinks per $1\n", result);
    
    return 0;
}
