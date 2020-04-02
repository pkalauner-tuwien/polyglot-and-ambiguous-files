import java.io.FileInputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

public class Zip {
	public static void main(String args[]) {
		if (args.length != 2) {
			System.err.println("Usage: java Zip <ZIP file>");
			System.exit(1);
		}

		try {
			ZipInputStream z = new ZipInputStream(new FileInputStream(args[1]));
			ZipEntry e;
			while ((e = z.getNextEntry()) != null) {
				System.out.println(e.getName());
			}
			z.close();
		} catch (FileNotFoundException fnfe) {
			System.err.println("Error: File does not exist.");
		} catch (IOException io) {
			System.err.println("Error: File could not be opened.");
		}
	}
}
