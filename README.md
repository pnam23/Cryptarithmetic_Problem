<h1>Cryptarithmetic Problem in AI</h1>
<h2>Overview</h2>
This project uses a genetic algorithm to solve a cryptorithmetic puzzle where each letter is associated with a particular digit. Finding a digit assignment that completes the equation is the goal. Through successive generations, the genetic algorithm iteratively develops potential solutions by using a population-centric strategy.
<h2>Requirements</h2>
Python3
<h2>Levels complexity</h2>
<h3>Level 1: Solve the addition equation or subtraction equation with 2 operands.</h3> 

<h3>Level 2: Solve any kind of equation with multiple operands and single operator (+ -).</h3>
For example:  
SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+
THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+ 
SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+ 
MAN+TRY+TO+MEET+THE+TEAM+ON+THE+ 
MOON+AS+HE+HAS+AT+THE+OTHER+TEN =TESTS 

The answer is that TRANHYSMOE=9876543210. 

<h3>Level 3: Solve any kind of equation with multiple operands and operators (+ - ).</h3>
We use the parentheses () are used to specify the order of operations. 
SEND+(MORE+MONEY)-OR+DIE=NUOYI 

The answers are SENDMORYIU=1369547082, 1658432970… 

<h3>Level 4: Solve level 3 with the multiplication equation (*).(2 operands, 1 operator)</h3> 
