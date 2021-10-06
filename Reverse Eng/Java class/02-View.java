import java.lang.reflect.Field;

class View
{
	public static void main(String[] args)
	{
		Countdown c = new Countdown();
		Field[] fields = Countdown.class.getDeclaredFields();
		int cycle;

		try
		{
			fields[0].setAccessible(true);
			cycle = (int)fields[0].get(c);
			System.out.println(cycle);
		} catch (Exception e) {}
	}
}
