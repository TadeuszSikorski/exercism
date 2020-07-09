using System;
using System.Linq;

public static class Hamming
{
    public static int Distance(string firstStrand, string secondStrand) => 
    ( firstStrand.Length != secondStrand.Length 
    ? throw new ArgumentException() 
    : firstStrand.Zip(secondStrand, (first, second) => first != second).Count(counter => counter));
}