using System;
using System.Linq;

public static class Pangram
{
    public static bool IsPangram(string input)
    {
        string alphabet = "abcdefghijklmnopqrstuvwxyz";

        if (string.IsNullOrWhiteSpace(input))
        {
            return false;
        }
        else
        {
            return alphabet.All(character => input.ToLower().Contains(character));
        }
        
    }
}
