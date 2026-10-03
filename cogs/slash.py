import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import olympus_embed

ALLOWED_GUILD_ID = 1555485039154827274

def allowed(interaction: discord.Interaction) -> bool:
    return interaction.guild_id == ALLOWED_GUILD_ID

async def deny(interaction):
    if not interaction.response.is_done():
        await interaction.response.send_message("Olympus is not available in this server.", ephemeral=True)

class RobuxPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Purchase Robux", style=discord.ButtonStyle.primary, custom_id="olympus:robux:purchase")
    async def purchase(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not allowed(interaction): return await deny(interaction)
        await interaction.response.send_message("Robux purchase workflow is ready for order configuration.", ephemeral=True)

class BloxPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Purchase Blox Fruits", style=discord.ButtonStyle.primary, custom_id="olympus:blox:purchase")
    async def purchase(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not allowed(interaction): return await deny(interaction)
        await interaction.response.send_message("Blox Fruits purchase workflow is ready for stock configuration.", ephemeral=True)

class AutoMMPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Create Auto Middleman", style=discord.ButtonStyle.primary, custom_id="olympus:automm:create")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not allowed(interaction): return await deny(interaction)
        await interaction.response.send_message("Auto Middleman workflow has been started.", ephemeral=True)

class ManualMMPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Request Middleman", style=discord.ButtonStyle.primary, custom_id="olympus:manualmm:create")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not allowed(interaction): return await deny(interaction)
        await interaction.response.send_message("Manual Middleman request has been started.", ephemeral=True)

POLICIES = {
"rules": ("SERVER RULES", """1. Respect members and staff.
2. No scams, impersonation, spam, unauthorized advertising, harassment, or malicious content.
3. Do not fabricate receipts, transaction IDs, messages, delivery evidence, or payment evidence.
4. Keep transactions inside official Olympus threads.
5. Never share passwords, OTPs, private keys, seed phrases, or recovery credentials.
6. Follow Discord rules and applicable platform/payment-provider rules."""),
"privacy": ("PRIVACY & LOGS", """Olympus may retain Discord user IDs, transaction IDs, timestamps, agreed deal terms, status changes, and evidence needed for transaction records or disputes.

Sensitive credentials must never be submitted. Transaction information should only be retained for legitimate operation, record keeping, safety, and dispute handling."""),
"tos": ("GENERAL TERMS", """Use accurate information and follow the exact terms confirmed inside the official transaction thread.

Fraud, impersonation, fabricated evidence, deceptive chargebacks, and attempts to manipulate transaction records are prohibited.

Each Olympus service also has its own service-specific terms."""),
"payment-terms": ("PAYMENT TERMS", """Verify the recipient, amount, currency, network, and payment details before sending funds.

A user's statement that payment was sent does not by itself verify payment. Olympus should mark a payment verified only after legitimate verification or authorized human confirmation.

Third-party payment-provider rules still apply."""),
"refund-terms": ("REFUND & CANCELLATION TERMS", """Refund eligibility depends on the transaction stage, payment method, delivery status, and terms confirmed for that transaction.

Irreversible transfers may not be recoverable. Olympus records a refund only after a real refund occurs."""),
"dispute-terms": ("DISPUTE & EVIDENCE TERMS", """Keep relevant evidence inside the official transaction thread.

Do not fabricate or manipulate receipts, transaction IDs, messages, or delivery evidence.

An active transaction may be paused while a legitimate dispute is reviewed. Both participants should cooperate with evidence requests."""),
"crypto-terms": ("CRYPTOCURRENCY TERMS", """Verify the asset, blockchain network, destination address, and amount before sending.

Blockchain transfers may be irreversible. A crypto payment must not be marked verified until the genuine transaction can be verified or an authorized human confirms it.

Never share private keys or seed phrases."""),
"robux-terms": ("ROBUX PURCHASE TERMS", """Confirm the Roblox account, Robux amount, rate, total price, and payment details before payment.

Delivery is recorded as completed only after the purchased order is actually fulfilled. Incorrect account information may delay delivery."""),
"blox-terms": ("BLOX FRUITS PURCHASE TERMS", """Confirm the product, quantity, stock, price, and delivery details before payment.

Stock availability should be confirmed before payment. Completion is recorded only after actual delivery."""),
"auto-mm-terms": ("AUTO MIDDLEMAN TERMS", """Both participants must confirm the exact exchange before the transaction proceeds.

Never transfer funds or assets because of an unsolicited DM claiming to be Olympus. Use only the official transaction workflow.

Release should occur only after the required verification and confirmations are complete."""),
"manual-mm-terms": ("MANUAL MIDDLEMAN TERMS", """Only the assigned authorized middleman should handle the exchange.

Both participants must confirm the exact deal terms. Keep communication, confirmations, and relevant evidence inside the official transaction thread.""")
}

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def policy(self, interaction, key):
        if not allowed(interaction): return await deny(interaction)
        title, text = POLICIES[key]
        await interaction.response.send_message(embed=olympus_embed(title, text), ephemeral=True)

    @app_commands.command(name="help", description="View all Olympus commands")
    async def help(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        text = """INFORMATION
/help /rules /privacy /support

TERMS
/tos /payment-terms /refund-terms /dispute-terms /crypto-terms

ROBUX
/robux-panel /robux-terms /robux-prices

BLOX FRUITS
/blox-panel /blox-terms /blox-stock /blox-prices

AUTO MM
/auto-mm-panel /auto-mm-terms /auto-mm-guide

MANUAL MM
/manual-mm-panel /manual-mm-terms /manual-mm-guide

TRANSACTIONS
/history /transaction

UTILITY
/say"""
        await interaction.response.send_message(embed=olympus_embed("HELP", text), ephemeral=True)

    @app_commands.command(name="rules", description="View Olympus server rules")
    async def rules(self, i): await self.policy(i, "rules")
    @app_commands.command(name="privacy", description="View privacy and logging policy")
    async def privacy(self, i): await self.policy(i, "privacy")
    @app_commands.command(name="tos", description="View general Olympus terms")
    async def tos(self, i): await self.policy(i, "tos")
    @app_commands.command(name="payment-terms", description="View payment terms")
    async def payment_terms(self, i): await self.policy(i, "payment-terms")
    @app_commands.command(name="refund-terms", description="View refund and cancellation terms")
    async def refund_terms(self, i): await self.policy(i, "refund-terms")
    @app_commands.command(name="dispute-terms", description="View dispute and evidence terms")
    async def dispute_terms(self, i): await self.policy(i, "dispute-terms")
    @app_commands.command(name="crypto-terms", description="View cryptocurrency terms")
    async def crypto_terms(self, i): await self.policy(i, "crypto-terms")
    @app_commands.command(name="robux-terms", description="View Robux purchase terms")
    async def robux_terms(self, i): await self.policy(i, "robux-terms")
    @app_commands.command(name="blox-terms", description="View Blox Fruits purchase terms")
    async def blox_terms(self, i): await self.policy(i, "blox-terms")
    @app_commands.command(name="auto-mm-terms", description="View Auto MM terms")
    async def auto_mm_terms(self, i): await self.policy(i, "auto-mm-terms")
    @app_commands.command(name="manual-mm-terms", description="View Manual MM terms")
    async def manual_mm_terms(self, i): await self.policy(i, "manual-mm-terms")

    @app_commands.command(name="support", description="View support information")
    async def support(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        await interaction.response.send_message(embed=olympus_embed("SUPPORT", "Use the official Olympus support process for purchase, middleman, payment, or transaction-record issues."), ephemeral=True)

    @app_commands.command(name="robux-panel", description="Post the Robux purchase panel")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def robux_panel(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        await interaction.channel.send(embed=olympus_embed("ROBUX PURCHASE", "Purchase Robux through Olympus. Review the current price and terms before continuing."), view=RobuxPanel())
        await interaction.response.send_message("Robux panel posted.", ephemeral=True)

    @app_commands.command(name="robux-prices", description="View Robux pricing")
    async def robux_prices(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("ROBUX PRICES", "Pricing has not been configured yet."), ephemeral=True)

    @app_commands.command(name="blox-panel", description="Post the Blox Fruits purchase panel")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def blox_panel(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        await interaction.channel.send(embed=olympus_embed("BLOX FRUITS MARKET", "Purchase available Blox Fruits stock through Olympus. Confirm stock and pricing before payment."), view=BloxPanel())
        await interaction.response.send_message("Blox Fruits panel posted.", ephemeral=True)

    @app_commands.command(name="blox-stock", description="View Blox Fruits stock")
    async def blox_stock(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("BLOX FRUITS STOCK", "Stock has not been configured yet."), ephemeral=True)

    @app_commands.command(name="blox-prices", description="View Blox Fruits pricing")
    async def blox_prices(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("BLOX FRUITS PRICES", "Pricing has not been configured yet."), ephemeral=True)

    @app_commands.command(name="auto-mm-panel", description="Post the Auto MM panel")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def auto_mm_panel(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        await interaction.channel.send(embed=olympus_embed("AUTO MIDDLEMAN", "Create an automated middleman transaction. Both participants must confirm the exact deal terms."), view=AutoMMPanel())
        await interaction.response.send_message("Auto MM panel posted.", ephemeral=True)

    @app_commands.command(name="auto-mm-guide", description="View the Auto MM process")
    async def auto_mm_guide(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("AUTO MIDDLEMAN GUIDE", "Agreement -> Both Confirm -> Deposit -> Verification -> Delivery -> Release -> Completed. A dispute option remains available while the transaction is active."), ephemeral=True)

    @app_commands.command(name="manual-mm-panel", description="Post the Manual MM panel")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def manual_mm_panel(self, interaction: discord.Interaction):
        if not allowed(interaction): return await deny(interaction)
        await interaction.channel.send(embed=olympus_embed("MANUAL MIDDLEMAN", "Request a human-assisted Olympus middleman transaction."), view=ManualMMPanel())
        await interaction.response.send_message("Manual MM panel posted.", ephemeral=True)

    @app_commands.command(name="manual-mm-guide", description="View the Manual MM process")
    async def manual_mm_guide(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("MANUAL MIDDLEMAN GUIDE", "Request -> Middleman Assigned -> Terms Confirmed -> Exchange -> Completion Confirmed -> Transaction Recorded."), ephemeral=True)

    @app_commands.command(name="history", description="View transaction history information")
    async def history(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=olympus_embed("TRANSACTION HISTORY", "Only genuinely completed Olympus transactions are recorded as completed."), ephemeral=True)

    @app_commands.command(name="transaction", description="Look up an Olympus transaction")
    @app_commands.describe(transaction_id="Example: AMM-0001")
    async def transaction(self, interaction: discord.Interaction, transaction_id: str):
        await interaction.response.send_message(embed=olympus_embed("TRANSACTION LOOKUP", f"Transaction: {transaction_id}\nNo verified stored record is available until the database workflow is connected."), ephemeral=True)

    @app_commands.command(name="say", description="Post an Olympus announcement")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.describe(message="Announcement text")
    async def say(self, interaction: discord.Interaction, message: str):
        if not allowed(interaction): return await deny(interaction)
        await interaction.channel.send(embed=olympus_embed("ANNOUNCEMENT", message))
        await interaction.response.send_message("Announcement posted.", ephemeral=True)

async def setup(bot):
    bot.add_view(RobuxPanel())
    bot.add_view(BloxPanel())
    bot.add_view(AutoMMPanel())
    bot.add_view(ManualMMPanel())
    await bot.add_cog(Slash(bot))
