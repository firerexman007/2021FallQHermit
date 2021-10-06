public class Countdown
{
	static int cycle = 2000000;

	public static void main(String[] args)
	{
		System.out.print("COUNTDOWN: ");
		while (cycle > 0)
		{
			System.out.print(cycle + ",");

			try
			{
				Thread.sleep(1000);
			} catch (Exception e) {}

			cycle--;
		}

		System.out.println("0");
		System.out.println("The password is c1c1c55407e1b2695e6cf49710b18774");
	}
}
