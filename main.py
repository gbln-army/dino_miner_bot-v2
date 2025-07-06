from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Ambil token dari environment variable atau langsung masukkan
TOKEN = os.environ.get("BOT_TOKEN") or "7527566683:AAE-LX8qpYKMk8Z-FGOEjytzKngpthVJdXc"
WEBHOOK_URL = "https://dino-miner-bot-v2.onrender.com"  # <- SESUAIKAN!

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or user.username or "Penambang"

    keyboard = [
        [InlineKeyboardButton("🪓 Mulai Menambang", callback_data="mine")],
        [InlineKeyboardButton("📊 Profil", callback_data="profile"),
         InlineKeyboardButton("🏪 Toko", callback_data="shop")],
        [InlineKeyboardButton("🎁 Airdrop", callback_data="airdrop")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = f"""🌋 Selamat Datang di 🌋  
🐾 *Jurassic Mining World* 🐾

👷‍♂️ Penambang: *{name}*
🎮 Level: 1
🪙 DinoCoin: 0
⛏️ Alat: Pickaxe Lv.1
🦖 Karakter: 🦕 Dino Basic

🎯 Tujuanmu: Tambang koin, buka karakter, dan jadi legenda dinosaurus!

───────────────
Pilih aksi di bawah ⬇️"""

    await update.message.reply_markdown(text, reply_markup=reply_markup)

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "mine":
        await query.edit_message_text("⛏️ Kamu mulai menambang... Tunggu hasilnya!")
    elif data == "profile":
        await query.edit_message_text("📊 Ini profil kamu...")
    elif data == "shop":
        await query.edit_message_text("🏪 Selamat datang di Toko Dino!")
    elif data == "airdrop":
        await query.edit_message_text("🎁 Kamu klaim 20 DinoCoin dari airdrop!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"{WEBHOOK_URL}/webhook"
    )
