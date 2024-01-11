package com.example;

import java.io.IOException;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import com.example.python3.Python3Lexer;
import com.example.python3.Python3Parser;
import com.example.python3.Python3Parser.File_inputContext;
import com.example.python3.*;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }



    /**
     * Says hello to the world.
     * 
     * @param args The arguments of the program.
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        if (args.length < 2) {
            System.out.println("Program <file> <mutation>");
        }
        CharStream stream = CharStreams.fromFileName(args[0]);
        Python3Lexer l = new Python3Lexer(stream);
        l.setTokenFactory(new CommonTokenFactory());
        Python3Parser p = new Python3Parser(new CommonTokenStream(l));

        File_inputContext ctx = p.file_input();

        ParseTreeVisitor<String> visitor = null;
        if (args[1].equals("syntax")) {
            visitor = new Obfuscator();
        } else if (args[1].equals("semantics")) {
            visitor = new Mutator();
        }
        else{
            System.out.printf("Wrong argument %s%n",args[1]);
            return;
        }
        System.out.println(visitor.visit(ctx));
    }
}
