// Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperature of the water.


// Q = waterMass ( finalTemperature – initialTemperature ) x 4184
// waterMass is water weight in kilograms
// finalTemperature and initialTemperature are temperatures in Celsius
// Q is the results in Joules

// Step 0: import Scanner library
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");

// Step #: set Scanner library to a variable
Scanner input = new Scanner(System.in);

// Step 1: Prompt the User to enter amount of water in kilograms(watermass)

System.out.print("\nEnter kilograms to the nearest decimal: ");
float kgFloat = input.nextFloat();
System.out.println("\nYou've Entered: " + kgFloat);

// Step 2: Prompt the User to enter initial temp. of the water
System.out.print("Enter initial temperature to the nearest decimal in Celsius: ");
float initialTemperature = input.nextFloat();
System.out.println("\nYou've Entered: " + initialTemperature);


// Step 3: Prompt the User to enter the final temp. of the water
System.out.print("Enter final temperature to the nearest decimal in Celsius: ");
float finalTemperature = input.nextFloat();
System.out.println("\nYou've Entered: " + finalTemperature);

// Step 4: Calculate 
// Q = watermass(kg) ( finalTemperature - initialTemperature ) * 4184

float temperature = finalTemperature - initialTemperature;
System.out.println("\nTemperature: " + temperature);

// Step 5: Give the output of the calculation 
System.out.print("\nEnter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
System.out.print("Enter final temperature to the nearest decimal in Celsius: \n");
// Step 6: Exit the program
// Step #: Close the input
input.close();
    }
}