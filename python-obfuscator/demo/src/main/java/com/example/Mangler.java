package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;

import org.antlr.v4.runtime.CommonToken;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.apache.commons.lang3.RandomStringUtils;

import com.example.python3.Python3Lexer;
import com.example.python3.Python3Parser;
import com.example.python3.Python3Parser.AnnassignContext;
import com.example.python3.Python3Parser.FuncdefContext;
import com.example.python3.Python3Parser.TestContext;
import com.example.python3.Python3ParserBaseListener;

public class Mangler extends Python3ParserBaseListener {
    Random rng = new Random();
    Set<String> identifiers = new HashSet<String>();
    Set<String> forbiddenSet = new HashSet<String>();
    Map<String, String> obfuscation = new HashMap<String, String>();
    {

        forbiddenSet.add("print");
        forbiddenSet.add("range");
        forbiddenSet.add("enumerate");
        forbiddenSet.add("rev");
        forbiddenSet.add("zip");
        forbiddenSet.add("map");
        forbiddenSet.add("tuple");
        forbiddenSet.add("index");
        forbiddenSet.add("list");
        forbiddenSet.add("set");
        forbiddenSet.add("next");
        forbiddenSet.add("insert");
        forbiddenSet.add("dict");
        forbiddenSet.add("len");
        forbiddenSet.add("remove");
        forbiddenSet.add("append");
        forbiddenSet.add("max");
        forbiddenSet.add("min");
        forbiddenSet.add("any");
        forbiddenSet.add("all");
        forbiddenSet.add("eval");
        forbiddenSet.add("push");
        forbiddenSet.add("pop");
        forbiddenSet.add("add");
        forbiddenSet.add("extend");
        forbiddenSet.add("reverse");
        forbiddenSet.add("sort");
    }
    int nameIndex = 0;

    StringBuilder x = new StringBuilder();


    @Override
    public void visitTerminal(TerminalNode node) {

        if (node.getSymbol().getType() == Python3Lexer.NAME
                && node.getParent().getParent() instanceof FuncdefContext) {
            forbiddenSet.add(node.getText()); // Ignore function definitions to ensure that they are called properly
        }
        if (node.getSymbol().getType() == Python3Lexer.NAME && !forbiddenSet.contains(node.getText())) {
            if (identifiers.add(node.getText())) {
                String x = String.format("var__%d",nameIndex++);
                obfuscation.put(node.getText(), x);
            }

            ((CommonToken) node.getSymbol()).setText(
                    obfuscation.get(node.getText()));

        }

        // if (node.getSymbol().getType() == Python3Lexer.NUMBER) {
        //     try {
        //         int x = Integer.valueOf(node.getText());
        //         int y = rng.nextInt(600);

        //         String eq = node.getText();
        //         switch (rng.nextInt(6)) {
        //             case 0:
        //                 eq = String.format("( (%d) + (%d) )", y, x - y);
        //                 break;
        //             case 1:
        //                 eq = String.format("( (%d) - (%d) )", y, y - x);
        //                 break;
        //             case 2:
        //                 eq = String.format("( ((%d) * (%d)) / (%d) )", x, y, y);
        //                 break;
        //             case 3:
        //                 eq = String.format("( ((%d) + (%d)) - (%d) )", x, y, y);
        //                 break;
        //             case 4:
        //                 eq = String.format("  ( (%d) ** 1 )", x);
        //             default:
        //                 eq = String.format(" ( -(-(-(-(%d)))) )", x);
        //                 break;
        //         }
        //         obfuscation.put(node.getText(), eq);
        //     } catch (NumberFormatException e) {
        //         // Was not an integer
        //     }
        // }

        if (node.getSymbol().getType() == Python3Lexer.STRING) {
            ArrayList<String> values = new ArrayList<String>();
            int noise = rng.nextInt(10);
            for (int i = 0; i < noise; i++) {
                values.add('"' + RandomStringUtils.randomAlphanumeric(2,rng.nextInt(10)+3) + '"');
            }

            int index = rng.nextInt(values.size());
            values.add(index, node.getSymbol().getText());

            obfuscation.put(node.getText(), values.toString() + String.format("[%d]", index));
        }
    }
}