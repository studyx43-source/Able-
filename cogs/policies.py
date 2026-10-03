from discord.ext import commands
from utils.embeds import olympus_embed

POLICIES = {
 "rules": ("SERVER RULES", "Respect members. No scams, impersonation, spam, unauthorized advertising, malicious content, or fabricated payment evidence. Keep transactions inside official Olympus threads. Never share passwords, OTPs, private keys, or recovery phrases."),
 "tos": ("TERMS OF SERVICE", "Use accurate transaction details and cooperate with legitimate dispute reviews. Fraud, deceptive chargebacks, impersonation, and fabricated evidence are prohibited."),
 "privacy": ("PRIVACY & LOGS", "Olympus may retain transaction IDs, Discord user IDs, timestamps, deal terms, status changes, and evidence needed for records and disputes. Never submit sensitive credentials."),
 "robuxtos": ("ROBUX PURCHASE TERMS", "Confirm the Roblox account, amount, price, and payment details before paying. Completion is recorded only after actual fulfillment."),
 "bloxtos": ("BLOX FRUITS PURCHASE TERMS", "Confirm stock, price, selected product, and delivery details before payment. Completion is recorded only after actual delivery."),
 "autommterms": ("AUTO MIDDLEMAN TERMS", "Both participants must confirm the exact deal. Never send assets from a DM claiming to be the bot. Payment or crypto status must be genuinely verified before being recorded as verified."),
 "manualmmterms": ("MANUAL MIDDLEMAN TERMS", "Only the assigned authorized middleman should handle the exchange. Both participants must confirm terms and keep evidence inside the official thread."),
 "refunds": ("REFUND POLICY", "Eligibility depends on transaction stage, payment method, delivery status, and agreed terms. A refund is recorded only when it actually occurs."),
 "disputes": ("DISPUTE POLICY", "Provide relevant evidence in the official thread. Do not edit or fabricate receipts, transaction IDs, messages, or delivery evidence.")
}

class Policies(commands.Cog):
    def __init__(self, bot): self.bot = bot

async def _send(ctx, key):
    title, body = POLICIES[key]
    await ctx.send(embed=olympus_embed(title, body))

def add_policy(name):
    async def command(self, ctx):
        await _send(ctx, name)
    command.__name__ = name
    return commands.command(name=name)(command)

for _name in POLICIES:
    setattr(Policies, _name, add_policy(_name))

async def setup(bot): await bot.add_cog(Policies(bot))
