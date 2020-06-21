using System;

public static class ResistorColor
{
    public static int ColorCode(string color) => Array.FindIndex(Colors(), resistorColor => resistorColor == color);

    public static string[] Colors() => new[] { "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white" };
}