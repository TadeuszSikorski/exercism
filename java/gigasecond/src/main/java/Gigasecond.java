import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {

	private LocalDateTime dateTime = null;

    public Gigasecond(LocalDate moment) {
        this.dateTime = moment.atStartOfDay();
    }

    public Gigasecond(LocalDateTime moment) {
        this.dateTime = moment;
    }

    public LocalDateTime getDateTime() {
        return this.dateTime.plusSeconds(1000000000L);
    }
}
