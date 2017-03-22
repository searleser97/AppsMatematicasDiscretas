/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kmap;

import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.*;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.UIManager.LookAndFeelInfo;
import javax.swing.UnsupportedLookAndFeelException;

public class Kmap extends JFrame {

    static String output = "";
    static int A[][] = new int[4][4];
    static int checked[][] = new int[4][4];
    static int value[] = new int[16];
    JButton btn[] = new JButton[16];
    JLabel lbl[] = new JLabel[10];
    JPanel table;
    JLabel text;
    JButton compute, reset;

    public Kmap() {
        JFrame f = new JFrame();
        f.setTitle("Mapa de Karnough por Sergio Sanchez");
        f.setSize(545, 395);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(EXIT_ON_CLOSE);
        f.setResizable(false);
        f.setLayout(null);
        f.setVisible(true);
        table = new JPanel();
        text = new JLabel();
        table.setBounds(135, 30, 400, 300);
        text.setBounds(10, 330, 580, 40);
        text.setBackground(Color.red);
        //ading button in table
        table.setLayout(new GridLayout(4, 4));

        for (int i = 0; i < 16; i++) {
            btn[i] = new JButton();

            btn[i].setIcon(new ImageIcon(System.getProperty("user.dir") + "/src/kmap/0.png"));
            table.add(btn[i]);
            table.validate();
            value[i] = 0;
        }
        //
        lbl[0] = new JLabel("A'B'");
        lbl[0].setBounds(110, 30, 30, 75);
        f.add(lbl[0]);
        lbl[1] = new JLabel("A'B");
        lbl[1].setBounds(110, 105, 30, 75);
        f.add(lbl[1]);
        lbl[2] = new JLabel("AB");
        lbl[2].setBounds(110, 180, 30, 75);
        f.add(lbl[2]);
        lbl[3] = new JLabel("AB'");
        lbl[3].setBounds(110, 255, 30, 75);
        f.add(lbl[3]);
        lbl[4] = new JLabel("C'D'");
        lbl[4].setBounds(160, 0, 80, 30);
        f.add(lbl[4]);
        lbl[5] = new JLabel("C'D");
        lbl[5].setBounds(260, 0, 80, 30);
        f.add(lbl[5]);
        lbl[6] = new JLabel("CD");
        lbl[6].setBounds(360, 0, 80, 30);
        f.add(lbl[6]);
        lbl[7] = new JLabel("CD'");
        lbl[7].setBounds(460, 0, 80, 30);
        f.add(lbl[7]);
        f.validate();
        //
        //button dading

        // f.add(button);
        compute = new JButton("Minimizar");
        compute.setBounds(5, 100, 90, 40);
        f.add(compute);
        reset = new JButton("Reiniciar");
        reset.setBounds(5, 160, 90, 40);
        f.add(reset);
        f.add(table);
        compute.validate();
        reset.validate();
        f.add(text);
        f.validate();
        
        f.repaint();
        
        //zero - one change change over
        for (int i = 0; i < 16; i++) {
            final int aux = i;
            btn[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    if (value[aux] == 1) {
                        value[aux] = 0;
                    } else {
                        value[aux] = 1;
                    }
                    //text.setText("value of btn[0]"+value[0]);
                    if (value[aux] == 0) {
                        btn[aux].setIcon(new ImageIcon(System.getProperty("user.dir") + "/src/kmap/0.png"));
                    }
                    if (value[aux] == 1) {
                        btn[aux].setIcon(new ImageIcon(System.getProperty("user.dir") + "/src/kmap/1.png"));
                    }
                }
            });
        }
        //reset
        reset.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                text.setText("");
                output = "";

                for (int i = 0; i < 16; i++) {
                    btn[i].setIcon(new ImageIcon(System.getProperty("user.dir") + "/src/kmap/0.png"));
                    value[i] = 0;
                }
            }
        });
        //compute
        compute.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {

                compute();
                text.setText("");

                text.setText("SOP=" + output.substring(1));

            }
        });
    }

    // initialize 2D-Array
    static void initialize() {
        int count = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                A[i][j] = value[count];
                checked[i][j] = 0;
                count++;
            }
        }
    }

    static void printMatrix(int A[][]) {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println("");
        }
    }
    //compute Algorithm for K-MAP

    static void compute() {
        initialize();
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (A[i][j] == 1 && checked[i][j] == 0) {
                    int pass8 = check8(i, j);
                    System.out.println("pass8: " + pass8);
                    if (pass8 == 0) {
                        int pass4 = check4(i, j);
                        System.out.println("pass4: " + pass4);
                        if (pass4 == 0) {
                            int pass2 = check2(i, j);
                            System.out.println("pass2: " + pass2);
                            if (pass2 == 0) {
                                nogrouping(i, j);
                            }
                        }
                    }
                }
            }
        }
        System.out.println("---------");

    }
    
    static int check8(int r, int c) {
        int result = 0;
        //case1
        if (A[r][0] == 1 && A[r][1] == 1 && A[r][2] == 1 && A[r][3] == 1 && A[r + 1][0] == 1 && A[r + 1][1] == 1 && A[r + 1][2] == 1 && A[r + 1][3] == 1) {
            String local = "";
            if (r == 0) {
                local = "A'";
            }
            if (r == 1) {
                local = "B";
            }
            if (r == 2) {
                local = "A";
            }
            if (r == 3) {
                local = "B'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][0] = 1;
            checked[r][1] = 1;
            checked[r][2] = 1;
            checked[r][3] = 1;
            checked[(r + 1) % 4][0] = 1;
            checked[(r + 1) % 4][1] = 1;
            checked[(r + 1) % 4][2] = 1;
            checked[(r + 1) % 4][3] = 1;
            // make it color
        } else //case2
        if (A[r][0] == 1 && A[r][1] == 1 && A[r][2] == 1 && A[r][3] == 1 && A[(4 + (r - 1)) % 4][0] == 1 && A[(4 + (r - 1)) % 4][1] == 1 && A[(4 + (r - 1)) % 4][2] == 1 && A[(4 + (r - 1)) % 4][3] == 1) {
            String local = "";
            if (r == 0) {
                local = "B'";
            }
            if (r == 1) {
                local = "A'";
            }
            if (r == 2) {
                local = "B";
            }
            if (r == 3) {
                local = "A";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][0] = 1;
            checked[r][1] = 1;
            checked[r][2] = 1;
            checked[r][3] = 1;
            checked[(4 + (r - 1)) % 4][0] = 1;
            checked[(4 + (r - 1)) % 4][1] = 1;
            checked[(4 + (r - 1)) % 4][2] = 1;
            checked[(4 + (r - 1)) % 4][3] = 1;
        } else //case3
        if (A[0][c] == 1 && A[1][c] == 1 && A[2][c] == 1 && A[3][c] == 1 && A[0][(c + 1) % 4] == 1 && A[1][(c + 1) % 4] == 1 && A[2][(c + 1) % 4] == 1 && A[3][(c + 1) % 4] == 1) {
            String local = "";
            if (c == 0) {
                local = "C'";
            }
            if (c == 1) {
                local = "D";
            }
            if (c == 2) {
                local = "C";
            }
            if (c == 3) {
                local = "D'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[0][c] = 1;
            checked[1][c] = 1;
            checked[2][c] = 1;
            checked[3][c] = 1;
            checked[0][(c + 1) % 4] = 1;
            checked[1][(c + 1) % 4] = 1;
            checked[2][(c + 1) % 4] = 1;
            checked[3][(c + 1) % 4] = 1;
        } else //case 4
        if (A[0][c] == 1 && A[1][c] == 1 && A[2][c] == 1 && A[3][c] == 1 && A[0][(4 + (c - 1)) % 4] == 1 && A[1][(4 + (c - 1)) % 4] == 1 && A[2][(4 + (c - 1)) % 4] == 1 && A[3][(4 + (c - 1)) % 4] == 1) {
            String local = "";
            if (c == 0) {
                local = "D'";
            }
            if (c == 1) {
                local = "C'";
            }
            if (c == 2) {
                local = "D";
            }
            if (c == 3) {
                local = "C";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[0][c] = 1;
            checked[1][c] = 1;
            checked[2][c] = 1;
            checked[3][c] = 1;
            checked[0][(4 + (c - 1)) % 4] = 1;
            checked[1][(4 + (c - 1)) % 4] = 1;
            checked[2][(4 + (c - 1)) % 4] = 1;
            checked[3][(4 + (c - 1)) % 4] = 1;
        }

        return result;
    }
    //ends of check8
    //check4 start

    static int check4(int r, int c) {
        int result = 0;
        String local = "";
        //case1
        if (A[r][0] == 1 && A[r][1] == 1 && A[r][2] == 1 && A[r][3] == 1) {
            if (r == 0) {
                local = "A'B'";
            }
            if (r == 1) {
                local = "A'B";
            }
            if (r == 2) {
                local = "AB";
            }
            if (r == 3) {
                local = "AB'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][0] = 1;
            checked[r][1] = 1;
            checked[r][2] = 1;
            checked[r][3] = 1;
        } else //case2
        if (A[0][c] == 1 && A[1][c] == 1 && A[2][c] == 1 && A[3][c] == 1) {
            if (c == 0) {
                local = "C'D'";
            }
            if (c == 1) {
                local = "C'D";
            }
            if (c == 2) {
                local = "CD";
            }
            if (c == 3) {
                local = "CD'";

            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[0][c] = 1;
            checked[1][c] = 1;
            checked[2][c] = 1;
            checked[3][c] = 1;
        } else //case3 row+ col+
        if (A[r][c] == 1 && A[r][(c + 1) % 4] == 1 && A[(r + 1) % 4][c] == 1 && A[(r + 1) % 4][(c + 1) % 4] == 1) {
            System.out.println("paso1");
            if (r == 0) {
                local = "A'";
            }
            if (r == 1) {
                local = "B";
            }
            if (r == 2) {
                local = "A";
            }
            if (r == 3) {
                local = "B'";
            }
            if (c == 0) {
                local = local + "C'";
            }
            if (c == 1) {
                local = local + "D";
            }
            if (c == 2) {
                local = local + "C";
            }
            if (c == 3) {
                local = local + "D'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][c] = 1;
            checked[r][(c + 1) % 4] = 1;
            checked[(r + 1) % 4][c] = 1;
            checked[(r + 1) % 4][(c + 1) % 4] = 1;
        } else //case4 row+ col--
        if (A[r][(4 + (c - 1)) % 4] == 1 && A[r][c] == 1 && A[(r + 1) % 4][(4 + (c - 1)) % 4] == 1 && A[(r + 1) % 4][c] == 1) {
            System.out.println("paso2");
            if (r == 0) {
                local = "A'";
            }
            if (r == 1) {
                local = "B";
            }
            if (r == 2) {
                local = "A";
            }
            if (r == 3) {
                local = "B'";
            }
            if (c == 0) {
                local = local + "D'";
            }
            if (c == 1) {
                local = local + "C'";
            }
            if (c == 2) {
                local = local + "D";
            }
            if (c == 3) {
                local = local + "C'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][(4 + (c - 1)) % 4] = 1;
            checked[r][c] = 1;
            checked[(r + 1) % 4][(4 + (c - 1)) % 4] = 1;
            checked[(r + 1) % 4][c] = 1;

        } else //case5 row - and col -
        if (A[(4 + (r - 1)) % 4][(4 + (c - 1)) % 4] == 1 && A[(4 + (r - 1)) % 4][c] == 1 && A[r][(4 + (c - 1)) % 4] == 1 && A[r][c] == 1) {
            System.out.println("paso3");
            if (r == 0) {
                local = "B'";
            }
            if (r == 1) {
                local = "A'";
            }
            if (r == 2) {
                local = "B";
            }
            if (r == 3) {
                local = "A";
            }
            if (c == 0) {
                local = local + "D'";
            }
            if (c == 1) {
                local = local + "C'";
            }
            if (c == 2) {
                local = local + "D";
            }
            if (c == 3) {
                local = local + "C'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[(4 + (r - 1)) % 4][(4 + (c - 1)) % 4] = 1;
            checked[(4 + (r - 1)) % 4][c] = 1;
            checked[r][(4 + (c - 1)) % 4] = 1;
            checked[r][c] = 1;
        } else //case6 row- col+
        if (A[(4 + (r - 1)) % 4][c] == 1 && A[(4 + (r - 1)) % 4][(c + 1) % 4] == 1 && A[r][c] == 1 && A[r][(c + 1) % 4] == 1) {
            if (r == 0) {
                local = "B'";
            }
            if (r == 1) {
                local = "A'";
            }
            if (r == 2) {
                local = "B";
            }
            if (r == 3) {
                local = "A";
            }
            if (c == 0) {
                local = local + "C'";
            }
            if (c == 1) {
                local = local + "D";
            }
            if (c == 2) {
                local = local + "C";
            }
            if (c == 3) {
                local = local + "D'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[(4 + (r - 1)) % 4][c] = 1;
            checked[(4 + (r - 1)) % 4][(c + 1) % 4] = 1;
            checked[r][c] = 1;
            checked[r][(c + 1) % 4] = 1;
        }

        return result;
    }
    //check for 2 check2

    static int check2(int r, int c) {
        int result = 0;
        String local = "";
        //case 1 col++
        if (A[r][c] == 1 && A[r][(c + 1) % 4] == 1) {
            if (r == 0) {
                local = "A'B'";
            }
            if (r == 1) {
                local = "A'B";
            }
            if (r == 2) {
                local = "AB";
            }
            if (r == 3) {
                local = "AB'";
            }
            if (c == 0) {
                local = local + "C'";
            }
            if (c == 1) {
                local = local + "D";
            }
            if (c == 2) {
                local = local + "C";
            }
            if (c == 3) {
                local = local + "D'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][c] = 1;
            checked[r][(c + 1) % 4] = 1;

        } else //case 2 col--
        if (A[r][(4 + (c - 1)) % 4] == 1 && A[r][c] == 1) {
            if (r == 0) {
                local = "A'B'";
            }
            if (r == 1) {
                local = "A'B";
            }
            if (r == 2) {
                local = "AB";
            }
            if (r == 3) {
                local = "AB'";
            }
            if (c == 0) {
                local = local + "D'";
            }
            if (c == 1) {
                local = local + "C'";
            }
            if (c == 2) {
                local = local + "D";
            }
            if (c == 3) {
                local = local + "C";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][(4 + (c - 1)) % 4] = 1;
            checked[r][c] = 1;
        } else //case3 row++
        if (A[r][c] == 1 && A[(r + 1) % 4][c] == 1) {
            if (r == 0) {
                local = "A'";
            }
            if (r == 1) {
                local = "B";
            }
            if (r == 2) {
                local = "A";
            }
            if (r == 3) {
                local = "B'";
            }
            if (c == 0) {
                local = local + "C'D'";
            }
            if (c == 1) {
                local = local + "C'D";
            }
            if (c == 2) {
                local = local + "CD";
            }
            if (c == 3) {
                local = local + "CD'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][c] = 1;
            checked[(r + 1) % 4][c] = 1;
        } else // case4 row--
        if (A[r][c] == 1 && A[(4 + (r - 1)) % 4][c] == 1) {
            if (r == 0) {
                local = "B'";
            }
            if (r == 1) {
                local = "A'";
            }
            if (r == 2) {
                local = "B";
            }
            if (r == 3) {
                local = "A";
            }
            if (c == 0) {
                local = local + "C'D'";
            }
            if (c == 1) {
                local = local + "C'D";
            }
            if (c == 2) {
                local = local + "CD";
            }
            if (c == 3) {
                local = local + "CD'";
            }
            output = output + "+" + local;
            result = 1;
            //make checked
            checked[r][c] = 1;
            checked[(4 + (r - 1)) % 4][c] = 1;
        }
        return result;
    }
    // no grouping

    static void nogrouping(int r, int c) {
        String local = "";
        if (r == 0) {
            local = "A'B'";
        }
        if (r == 1) {
            local = "A'B";
        }
        if (r == 2) {
            local = "AB";
        }
        if (r == 3) {
            local = "AB'";
        }
        if (c == 0) {
            local = local + "C'D'";
        }
        if (c == 1) {
            local = local + "C'D";
        }
        if (c == 2) {
            local = local + "CD";
        }
        if (c == 3) {
            local = local + "CD'";
        }
        output = output + "+" + local;

        checked[r][c] = 1;
    }

    public static void main(String args[]) {
        try {
            for (LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception e) {
            try {
                UIManager.setLookAndFeel(
                        UIManager.getCrossPlatformLookAndFeelClassName());
            } catch (ClassNotFoundException ex) {
                Logger.getLogger(Kmap.class.getName()).log(Level.SEVERE, null, ex);
            } catch (InstantiationException ex) {
                Logger.getLogger(Kmap.class.getName()).log(Level.SEVERE, null, ex);
            } catch (IllegalAccessException ex) {
                Logger.getLogger(Kmap.class.getName()).log(Level.SEVERE, null, ex);
            } catch (UnsupportedLookAndFeelException ex) {
                Logger.getLogger(Kmap.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        Kmap object = new Kmap();
    }

}
