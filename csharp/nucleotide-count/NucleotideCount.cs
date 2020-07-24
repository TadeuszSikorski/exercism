using System;
using System.Collections.Generic;
using System.Linq;

public static class NucleotideCount
{
    public static IDictionary<char, int> Count(string sequence) =>
        !sequence.All(nucleotide => "ACGT".Contains(nucleotide)) 
        ? throw new ArgumentException() 
        : "ACGT".ToDictionary(
            nucleotide => nucleotide, 
            nucleotide => sequence.Count(character => character == nucleotide));
}
