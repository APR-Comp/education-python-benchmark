package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;
import java.util.stream.Stream;

import org.antlr.v4.runtime.CommonToken;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.RuleNode;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.apache.commons.lang3.RandomStringUtils;

import com.example.python3.Python3Lexer;
import com.example.python3.Python3Parser;
import com.example.python3.Python3Parser.AnnassignContext;
import com.example.python3.Python3Parser.Comp_opContext;
import com.example.python3.Python3Parser.ExprContext;
import com.example.python3.Python3Parser.For_stmtContext;
import com.example.python3.Python3Parser.FuncdefContext;
import com.example.python3.Python3Parser.If_stmtContext;
import com.example.python3.Python3Parser.Return_stmtContext;
import com.example.python3.Python3Parser.StmtContext;
import com.example.python3.Python3Parser.TestContext;
import com.example.python3.Python3ParserBaseListener;
import com.example.python3.Python3ParserBaseVisitor;

public class Mutator extends Python3ParserBaseVisitor<String> {
    boolean hasBroken = false;
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
    int indents = 0;
    final int indentationConstant = 2;

    StringBuilder x = new StringBuilder();

    @Override
    public String visitChildren(RuleNode node) {
        String result = "";
        int n = node.getChildCount();
        for (int i = 0; i < n; i++) {
            if (!shouldVisitNextChild(node, result)) {
                break;
            }

            ParseTree c = node.getChild(i);
            String childResult = c.accept(this);
            result = aggregateResult(result, childResult);
        }

        return result;
    }

    // @Override
    // public String visitStmt(StmtContext ctx) {
    // if(rng.nextInt(100) < 40){
    // return super.visitStmt(ctx);
    // }
    // else{
    // String indent = " ".repeat(indentationConstant);
    // String baseIndent = " ".repeat(indentationConstant * indents);
    // String newIndent = " ".repeat(indentationConstant * (indents+1));
    // indents++;
    // String body = visit(ctx.children.get(0));
    // if (body.startsWith("\n")) {
    // body = body.trim();
    // }
    // indents--;
    // StringBuilder x = new StringBuilder();
    // x.append(indent)
    // .append("if True:\n")
    // .append(newIndent);

    // x
    // .append(body)
    // .append("\n");
    // return x.toString();
    // }
    // }

    @Override
    public String visitFor_stmt(For_stmtContext ctx) {
        String indent = " ".repeat(indentationConstant);
        String baseIndents = " ".repeat(indentationConstant * indents);
        String tryInnerIndents = " ".repeat(indentationConstant * (indents + 1));
        String bodyIndents = " ".repeat(indentationConstant * (indents + 2));
        StringBuilder x = new StringBuilder();

        indents++;
        String expressions = visit(ctx.exprlist());
        String body = visit(ctx.block(0));
        if (body.startsWith("\n")) {
            body = body.trim();
        }
        indents--;

        String iteratorName = RandomStringUtils.randomAlphabetic(2, rng.nextInt(10) + 3);
        String iterator = visit(ctx.testlist());

        x.append(indent)
                .append("try:\n")
                .append(tryInnerIndents)
                .append(iteratorName)
                .append("=")
                .append("iter(")
                .append(iterator)
                .append(")\n")
                .append(tryInnerIndents)
                .append("while True:\n")
                .append(bodyIndents)
                .append(expressions)
                .append("=")
                .append("next(")
                .append(iteratorName)
                .append(")\n")
                .append(bodyIndents)
                .append(body)
                .append('\n')
                .append(baseIndents)
                .append("except StopIteration:\n")
                .append(tryInnerIndents)
                .append("pass\n");
        ;

        if (ctx.ELSE() != null) {
            x.append("finally:\n")
                    .append(visit(ctx.block(1)));
        }
        return x.toString();
    }

    static List<String> ops = List.of("+", "-", ">>", "<<", "*", "%", "/", "^", "&", "|");

    @Override
    public String visitExpr(ExprContext ctx) {
        if (hasBroken || rng.nextInt(100) < 40) {
            return super.visitExpr(ctx);
        }
        if (ctx.expr() == null || ctx.expr().size() == 0) {
            return super.visitExpr(ctx);
        } else {
            hasBroken = true;
            if (!(ctx.getChild(0) instanceof ExprContext)) {
                return visit(ctx.getChild(ctx.children.size() - 1));// Skip all the ops
            } else {
                Stream<String> expressions = ctx.expr().stream().map(this::visit);
                String expression = visit(ctx.children.get(1));
                final String temp;
                switch (expression) {

                    case "-":
                        temp = "+";
                        break;

                    case "+":
                        temp = "-";
                        break;

                    case ">>":
                        temp = "<<";
                        break;

                    case "<<":
                        temp = ">>";
                        break;

                    case "/":
                        temp = "%";
                        break;

                    case "%":
                        temp = "/";
                        break;

                    case "|":
                        temp = "&";
                        break;

                    case "&":
                        temp = "|";
                        break;

                    case "^":
                        temp = "&";
                        break;

                    default:
                        temp = expression;
                }
                return expressions.reduce( (a , b) -> a + temp + b ).orElseThrow();
            }

        }
    }

    List<String> compOps = List.of(">","<","==","!=",">=","<=");
    @Override
    public String visitComp_op(Comp_opContext ctx) {
        if(hasBroken || rng.nextInt(100) < 30){
            return super.visitComp_op(ctx);
        }
        
        hasBroken=true;
        if (ctx.children.size() == 2) {
            int index = 0;
            if (((TerminalNode) ctx.getChild(0)).getSymbol().getType() == Python3Lexer.NOT) {
                index++;
            }
            return visit(ctx.getChild(index));
        } else {     
            switch(ctx.children.get(0).getText()){
                case "in":
                return "not in";
                case "is":
                return "is not";
                default: 
                {
                    String x = compOps.get(rng.nextInt(compOps.size()));
                    while(x.equals(ctx.getChild(0).getText())){
                        x = compOps.get(rng.nextInt(compOps.size()));
                    }
                    return x;
                }
            }
        }
    }

    @Override
    public String visitReturn_stmt(Return_stmtContext ctx) {
        String res = super.visitReturn_stmt(ctx);
        if (!hasBroken && rng.nextInt(100) < 40) {
            hasBroken = true;
            if (rng.nextBoolean()) {
                return "\n";
            } else {
                return res.split("return ")[1];
            }
        }

        else {
            return res;
        }
        // TODO Auto-generated method stub
    }

    @Override
    public String visitIf_stmt(If_stmtContext ctx) {
        if (ctx.ELSE() == null &&
                (ctx.ELIF() == null || ctx.ELIF().size() == 0)) {

            String indent = " ".repeat(indentationConstant);
            String initialIndents = " ".repeat(indentationConstant * (indents));
            String test = visit(ctx.test(0));
            indents++;
            String body = visit(ctx.block(0));
            if (body.startsWith("\n")) {
                body = body.trim();
            }
            indents--;
            String newIndents = " ".repeat(indentationConstant * (indents + 1));

            String err = "not";
            if (!hasBroken && rng.nextInt(100) < 40) {
                hasBroken = true;
                err = "";
            }
            StringBuilder x = new StringBuilder();
            x.append(indent)
                    .append("if ")
                    .append(err)
                    .append(" ")
                    .append(test)
                    .append(":\n")
                    .append(newIndents)
                    .append("pass\n")
                    .append(initialIndents)
                    .append("else:\n")
                    .append(newIndents)
                    .append(body)
                    .append("\n");

            return x.toString();
        }
        if (ctx.ELSE() != null &&
                (ctx.ELIF() == null || ctx.ELIF().size() == 0)) {

            String indent = " ".repeat(indentationConstant);
            String initialIndents = " ".repeat(indentationConstant * (indents));
            String test = visit(ctx.test(0));

            indents++;
            String body = visit(ctx.block(0));
            if (body.startsWith("\n")) {
                body = body.trim();
            }
            String elseBody = visit(ctx.block(1));
            if (elseBody.startsWith("\n")) {
                elseBody = elseBody.trim();
            }
            indents--;

            String newIndents = " ".repeat(indentationConstant * (indents + 1));

            String err = "not";
            if (!hasBroken && rng.nextInt(100) < 40) {
                hasBroken = true;
                err = "";
            }

            StringBuilder x = new StringBuilder();
            x.append(indent)
                    .append("if ")
                    .append(err)
                    .append(" ")
                    .append(test)
                    .append(":\n")
                    .append(newIndents)
                    .append(elseBody)
                    .append("\n")
                    .append(initialIndents)
                    .append("else:\n")
                    .append(newIndents)
                    .append(body)
                    .append("\n");

            return x.toString();
        }

        return super.visitIf_stmt(ctx);
    }

    /**
     * {@inheritDoc}
     *
     * <p>
     * The default implementation returns the result of
     * {@link #defaultResult defaultResult}.
     * </p>
     */
    @Override
    public String visitTerminal(TerminalNode node) {

        if (node.getSymbol().getType() == Python3Lexer.NAME
                && node.getParent().getParent() instanceof FuncdefContext) {
            forbiddenSet.add(node.getText()); // Ignore function definitions to ensure that they are called properly
        }
        if (node.getSymbol().getType() == Python3Lexer.NAME && !forbiddenSet.contains(node.getText())) {
            if (identifiers.add(node.getText())) {
                String x = String.format("var__%d", nameIndex++);
                obfuscation.put(node.getText(), x);
            }

            ((CommonToken) node.getSymbol()).setText(
                    obfuscation.get(node.getText()));

        }

        if (node.getSymbol().getType() == Python3Lexer.INDENT) {
            /// System.out.println("FOUND INDENT");
            indents++;
            return " ".repeat(indentationConstant);
        }
        if (node.getSymbol().getType() == Python3Lexer.DEDENT) {
            // System.out.println("FOUND DEDENT");
            indents--;
        }

        if (node.getSymbol().getType() == Python3Lexer.NUMBER && !hasBroken && rng.nextInt(100) < 40) {
            try {
                int offset = (rng.nextInt(6) - 3);
                while (offset == 0) {
                    offset = (rng.nextInt(6) - 3);
                }
                String x = String.valueOf(Integer.valueOf(node.getText()) + offset);
                hasBroken = true;
                return x;
            } catch (NumberFormatException e) {
                // Was not an integer
            }
        }

        return node.getText().replace("\t", " ".repeat(indentationConstant));
    }

    /**
     * {@inheritDoc}
     *
     * <p>
     * The default implementation returns the result of
     * {@link #defaultResult defaultResult}.
     * </p>
     */
    @Override
    public String visitErrorNode(ErrorNode node) {
        return null;
    }

    /**
     * Gets the default value returned by visitor methods. This value is
     * returned by the default implementations of
     * {@link #visitTerminal visitTerminal}, {@link #visitErrorNode visitErrorNode}.
     * The default implementation of {@link #visitChildren visitChildren}
     * initializes its aggregate result to this value.
     *
     * <p>
     * The base implementation returns {@code null}.
     * </p>
     *
     * @return The default value returned by visitor methods.
     */
    protected String defaultResult() {
        return "";// " ".repeat(indents * 4);
    }

    @Override
    protected String aggregateResult(String aggregate, String nextResult) {
        // System.out.printf("aggregating '%s' '%s' %n",aggregate,nextResult);
        if (nextResult == "<EOF>" || nextResult == null)
            return aggregate == null ? "" : aggregate;
        if (aggregate == "" || aggregate == null)
            return nextResult;
        // if(aggregate.endsWith(" ".repeat(indents*2)))
        // return aggregate + nextResult;
        if (aggregate.endsWith("\n")) {
            String indentation = " ".repeat(indentationConstant * indents);
            if (nextResult.startsWith(" ")) {
                return aggregate + nextResult;
            } else {
                return aggregate + indentation + nextResult;
            }
        } else if (aggregate.endsWith(" ")) {
            return aggregate + nextResult;
        } else {
            return aggregate + " " + nextResult;
        }
    }
}