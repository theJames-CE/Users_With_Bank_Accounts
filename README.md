<h1>Assignment: Users with Bank Accounts</h1>

<b>Welcome to another Core assignment!</b><br>

Some students like to explore the assignments before they're finished reading through the lessons, and that's okay! It can be good for your brain to have a preview of what your future challenges might be. However, before you begin this assignment, it's important that you've first:

<li>Completed the preceding lesson modules</li><br>
<li>Taken the knowledge checks to confirm your understanding</li><br>
<li>Viewed lecture material related to the assignment topics</li><br>
<li>Completed and submitted your practice assignments</li><br>

<h2>Now, the Assignment:</h2>

Create a <b><i>User</b></i> class that has an association with the <b><i>BankAccoun</b></i>t class. You should not have to change anything in the <b><i>BankAccount</b></i> class.

For example, from the User class we should be able to deposit money into the user's account:

![image](https://github.com/theJames-CE/Users_With_Bank_Accounts/assets/124546382/ad271585-532b-456c-a22e-5d70049edd84)

But our <b><i>User </b></i>class does not have a <b><i>self.account_balance</b></i> attribute. What it does have is an <i>instance</i> of a BankAccount by the name of <b><i>self.account</b></i>. That means that we'll be mirroring the methods created in the <b><i>BankAccount</b></i> class like make_deposit (and other methods referencing self.account_balance). But we'll be calling on the <b><i>BankAccount</b></i> class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.

Remember in our User methods, we can now access the <b><i>BankAccount</b></i> class through our <b><i>self.account attribute</b></i>, like so:

![image](https://github.com/theJames-CE/Users_With_Bank_Accounts/assets/124546382/b499e6fa-d446-4257-bfb3-033ba8d4bdfe)

<h3>Example Display for Sensei bonus</h3>

![image](https://github.com/theJames-CE/Users_With_Bank_Accounts/assets/124546382/4d1dcb3f-7b53-4b17-b29e-bb4463f66a77)

![image](https://github.com/theJames-CE/Users_With_Bank_Accounts/assets/124546382/0e835a0c-a9ff-4665-abb2-ef13f82b7d83)

#CodingDojo
