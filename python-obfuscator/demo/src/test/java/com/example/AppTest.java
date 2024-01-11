package com.example;

import org.junit.jupiter.api.Test;

import com.example.python3.Python3Lexer;
import com.example.python3.Python3Parser;
import com.example.python3.Python3Parser.File_inputContext;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

/**
 * Unit test for simple App.
 */
class AppTest {
    /**
     * Rigorous Test.
     */
    //@Test
    void testMangler() {
String s ="""
def x (z):
    y = 2
    \"23\"
    if a:
        y = 3
    print(y)

def unique_day(date, possible_birthdays):
    count = 0
    print(count)
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 

""";

        CharStream stream = CharStreams.fromString(s);
        Python3Lexer l = new Python3Lexer(stream);
        Python3Parser p = new Python3Parser(new CommonTokenStream(l));

        File_inputContext ctx = p.file_input();

        ParseTreeWalker walker = new ParseTreeWalker();
        Mangler mangler = new Mangler();
        walker.walk(mangler,ctx);
        // System.out.println("Allowed");
        // mangler.identifiers.forEach(System.out::println);
        // System.out.println("Forbidden");
        // mangler.forbiddenSet.forEach(System.out::println);

        System.out.println("Mapping");
        mangler.obfuscation.forEach((k,v) -> System.out.printf("%s -> %s%n",k,v) );

        System.out.println("New text");
        System.out.println(mangler.x.toString());
        l.reset();
        l.getAllTokens().forEach( x -> System.out.print(mangler.obfuscation.getOrDefault(x.getText(), x.getText())));
        
    }

    //@Test
    void testObfuscator() {
String s ="""
def x (z):
    y = 2
    \"23\"
    if birthday[1] == day:
        count += 1
    else:
        count += 2
    if birthday[1] == day:
        count += 1
    print(y)

def unique_day(date, possible_birthdays):
    count = 0
    print(count)
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 

""";

        CharStream stream = CharStreams.fromString(s);
        Python3Lexer l = new Python3Lexer(stream);
        Python3Parser p = new Python3Parser(new CommonTokenStream(l));

        File_inputContext ctx = p.file_input();


        Obfuscator obfuscator = new Obfuscator();
        // System.out.println("Allowed");
        // mangler.identifiers.forEach(System.out::println);
        // System.out.println("Forbidden");
        // mangler.forbiddenSet.forEach(System.out::println);
        
        System.out.println("Mapping");
        System.out.println(obfuscator.visit(ctx));
    }


    @Test
    void testMutator() {
String s ="""
def x (z):
    y = 2
    \"23\"
    if birthday[1] == day:
        count += 1
    else:
        count += 2
    if birthday[1] == day:
        count += 1
    print(y)

def unique_day(date, possible_birthdays):
    count = 0
    print(count)
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 

""";

        CharStream stream = CharStreams.fromString(s);
        Python3Lexer l = new Python3Lexer(stream);
        Python3Parser p = new Python3Parser(new CommonTokenStream(l));

        File_inputContext ctx = p.file_input();


        Mutator mutator = new Mutator();
        // System.out.println("Allowed");
        // mangler.identifiers.forEach(System.out::println);
        // System.out.println("Forbidden");
        // mangler.forbiddenSet.forEach(System.out::println);
        
        System.out.println("Mapping");
        System.out.println(mutator.visit(ctx));
        System.out.printf("Did I mutate %b?%n",mutator.hasBroken);
    }

}
