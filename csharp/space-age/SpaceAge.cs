using System;

public class SpaceAge
{
    private const double earthOrbitalPeriodInSecond = 31557600.0;
    private const double mercuryOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 0.2408467;
    private const double venusOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 0.61519726;
    private const double marsOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 1.8808158;
    private const double jupiterOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 11.862615;
    private const double saturnOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 29.447498;
    private const double uranusOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 84.016846;
    private const double neptuneOrbitalPeriodInSecond = earthOrbitalPeriodInSecond * 164.79132;

    private int ageInSeconds;

    public SpaceAge(int seconds)
    {
        this.ageInSeconds = seconds;
    }

    public double OnEarth() => ageInSeconds / earthOrbitalPeriodInSecond;

    public double OnMercury() =>  ageInSeconds / mercuryOrbitalPeriodInSecond;

    public double OnVenus() => ageInSeconds / venusOrbitalPeriodInSecond;

    public double OnMars() => ageInSeconds / marsOrbitalPeriodInSecond;

    public double OnJupiter() => ageInSeconds / jupiterOrbitalPeriodInSecond;

    public double OnSaturn() => ageInSeconds / saturnOrbitalPeriodInSecond;

    public double OnUranus() => ageInSeconds / uranusOrbitalPeriodInSecond;

    public double OnNeptune() => ageInSeconds / neptuneOrbitalPeriodInSecond;
}