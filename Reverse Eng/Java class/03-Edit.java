import java.lang.reflect.Field;

class Edit
{
	public static void main(String[] args)
	{
		Countdown c = new Countdown();
		Field[] fields = Countdown.class.getDeclaredFields();

		try
		{
			fields[0].setAccessible(true);
			fields[0].set(c, 10);
			c.main(null);
		} catch (Exception e) {}
	}
}
