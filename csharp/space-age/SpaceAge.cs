using System;

public class SpaceAge
{
    private double earthOrbitalPeriodInSecond = 31557600.0;
    private int ageInSeconds;

    public SpaceAge(int seconds)
    {
        ageInSeconds = seconds;
    }

    private double GetPlanetOrbitalPeriodInSecond(double orbitalPeriodInEarthYears) => earthOrbitalPeriodInSecond * orbitalPeriodInEarthYears;

    public double OnEarth() => Math.Round(ageInSeconds / earthOrbitalPeriodInSecond, 2);

    public double OnMercury() =>  Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(0.2408467), 2);

    public double OnVenus() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(0.61519726), 2);

    public double OnMars() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(1.8808158), 2);

    public double OnJupiter() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(11.862615), 2);

    public double OnSaturn() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(29.447498), 2);

    public double OnUranus() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(84.016846), 2);

    public double OnNeptune() => Math.Round(ageInSeconds / GetPlanetOrbitalPeriodInSecond(164.79132), 2);
}