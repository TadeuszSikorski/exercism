using System;
using System.Collections.Generic;
using System.Linq;

public static class Isogram
{
    public static bool IsIsogram(string word) => 
        word.ToLower()
            .Where(Char.IsLetter)
            .GroupBy(letter => letter)
            .All(letter => letter.Count() == 1);
}
