

package csci2011.lab8;

/**
 *
 * @author Joshua Ballard
 */
import java.io.File;

import java.io.FileNotFoundException;

import java.io.FileOutputStream;

import java.io.PrintWriter;

import java.util.Scanner;
public class Ballardlab8 {

    /**
     * @param args the command line arguments
     */
 



public static PrintWriter openFileForWriting(String filename) {

try {

PrintWriter printWriter = new PrintWriter(filename);

return printWriter;

} catch (FileNotFoundException e) {

System.out.println("The file does not exist");

System.exit(0);

}

return null;

}

public static PrintWriter openFileForAppending(String filename) {

try {

PrintWriter printWriter = new PrintWriter(new FileOutputStream(

new File(filename),

true /* append = true */));

return printWriter;

} catch (FileNotFoundException e) {

System.out.println("The file does not exist");

System.exit(0);

}

return null;

}

public static int readLinesFromFile(Scanner reader) {

int lines = 0;

while (reader.hasNextLine()) {

String data = reader.nextLine();

lines++;

System.out.println(data);

}

return lines;

}

public static int writeLinesToFile(PrintWriter printWriter) {

Scanner s = new Scanner(System.in);

int counter = 0;

if (printWriter != null) {

System.out.println("Enter the text you want to write to the file. Enter a blank line when you are done.");

while (true) {

String line = s.nextLine();

if (line.length()==0) {

break;

} else {

printWriter.println(line);

printWriter.flush();

counter++;

}

}

}

return counter;

}

public static void main(String[] args) {

String path = "C:\\Users\\Balla\\OneDrive\\Desktop\\Lab Assignments\\Lab8";

String filename = "hello.txt";

System.out.println("Opened file " + filename + " for writing");

PrintWriter printWriter = openFileForWriting(path+filename);

int lines = writeLinesToFile(printWriter);

System.out.println("Wrote " + lines + " lines to " + filename);

try {

System.out.println("Opened file " + filename + " for reading");

Scanner reader = new Scanner(new File(path+filename));

int readLines = readLinesFromFile(reader);

System.out.println("Read " + readLines + " lines from " + filename);

} catch (FileNotFoundException e) {

System.out.println("The file does not exist");

System.exit(0);

}

PrintWriter append = openFileForAppending(path+filename);

System.out.println("Opened file " + filename + " for appending");

lines = writeLinesToFile(append);

System.out.println("Wrote " + lines + " lines to " + filename);

try {

System.out.println("Opened file " + filename + " for reading");

Scanner reader = new Scanner(new File(path+filename));

int readLines = readLinesFromFile(reader);

System.out.println("Read " + readLines + " lines from " + filename);

} catch (FileNotFoundException e) {

System.out.println("The file does not exist");

System.exit(0);

}

}

}
