public class Hamming {
    private String leftStrandString;
    private String rightStrandString;
    private int distance;
    
    public Hamming(String leftStrand, String rightStrand) {
        if (checkInputValues(leftStrand, rightStrand))
        {
            this.leftStrandString = leftStrand;
            this.rightStrandString = rightStrand;
        }
        
        this.distance = 0;
    }

    private boolean checkInputValues(String leftStrand, String rightStrand)
    {
        if (leftStrand.isEmpty() && rightStrand != "")
        {
            throw new IllegalArgumentException("left strand must not be empty.");
        }
        else if (leftStrand != "" && rightStrand.isEmpty()) 
        {
            throw new IllegalArgumentException("right strand must not be empty.");
        }
        else if (leftStrand.length() != rightStrand.length())
        {
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }
        else
        {
            return true;
        }
    }

    public int getHammingDistance() {
        for(int index = 0; index < this.leftStrandString.length(); index++)
        {
            if (this.leftStrandString.charAt(index) != this.rightStrandString.charAt(index))
            {
                this.distance += 1;
            }
        }
        
        return this.distance;
    }
}
