import discord
from discord import app_commands
from discord.ext import commands

GUILD = discord.Object(id=1555485039154827274)

def make_embed(title, text):
    e = discord.Embed(title=title, description=text)
    e.set_footer(text="Olympus Middleman & Marketplace")
    return e

RULES = """**1. Conduct**
Treat members and staff respectfully. Harassment, threats, disruptive spam, malicious content, and deliberate interference with transactions or support are prohibited.

**2. Official Transactions**
Use official Olympus systems for transactions. Verify the item, amount, price, participants, and delivery terms before proceeding. Do not impersonate Olympus staff, middlemen, or automated systems.

**3. Honest Evidence**
Transaction information must be accurate. Fabricated or manipulated receipts, transaction IDs, payment claims, chat evidence, delivery evidence, or vouches are prohibited.

**4. Account Security**
Never share passwords, one-time codes, private keys, seed phrases, or recovery credentials. Staff should not request credentials unnecessary for a service.

**5. Transaction Areas**
Keep relevant transaction discussion and evidence inside the official Olympus transaction area. Do not intentionally disrupt another user's transaction or support process.

**6. Platform Rules**
Users remain responsible for following Discord rules and applicable rules of games, marketplaces, and payment providers."""

TOS = """**1. Agreement**
Review all transaction details before proceeding. Do not confirm incorrect or incomplete information.

**2. Official Workflow**
Use official Olympus systems and verify the participants before proceeding.

**3. Payments**
Verify the recipient, amount, currency, payment method, and network where applicable. A screenshot or payment claim does not by itself verify payment.

**4. Delivery and Completion**
A transaction is completed only after the agreed item, service, payment, or exchange has actually been completed.

**5. Refunds and Cancellations**
Eligibility may depend on transaction stage, delivery status, payment method, and applicable service terms. Some transfers may be irreversible.

**6. Disputes**
Keep relevant evidence connected to the official transaction. Fabricated or deliberately misleading evidence is prohibited.

**7. User Responsibility**
Check usernames, amounts, items, payment information, wallet addresses, networks, and other important details before confirming.

**8. Security**
Never provide passwords, one-time codes, private keys, seed phrases, or account recovery credentials.

**9. Fraud and False Information**
Fake payment claims, fabricated transaction IDs, fake receipts, manipulated evidence, impersonation, and false delivery claims are prohibited.

**10. Service-Specific Terms**
Different Olympus services may have additional terms relevant to their individual workflows.

**11. Third-Party Services**
Third-party platforms and payment providers have their own rules and limitations. Users remain responsible for complying with them.

**12. Final Confirmation**
Before confirming any transaction, verify the participants, item or service, amount, payment information, delivery terms, and applicable terms."""

class Policies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rules", description="Post the Olympus server rules")
    @app_commands.guilds(GUILD)
    async def rules(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=make_embed("OLYMPUS | SERVER RULES", RULES))

    @app_commands.command(name="tos", description="Post the Olympus Terms of Service")
    @app_commands.guilds(GUILD)
    async def tos(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=make_embed("OLYMPUS | TERMS OF SERVICE", TOS))

async def setup(bot):
    await bot.add_cog(Policies(bot))
