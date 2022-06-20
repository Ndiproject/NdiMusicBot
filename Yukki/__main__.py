import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (LOG_GROUP_ID, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, SUDOERS, app, random_assistant)
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Core.PyTgCalls.Yukki import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Yukki.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Inline import private_panel
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.inline import paginate_modules

try:
    from config import START_IMG_URL
except:
    START_IMG_URL = None


loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Menyelesaikan Memulai Ulang...",
    ) as status:
        ass_count = len(random_assistant)
        if ass_count == 0:
            console.print(
                f"\n[red] Tidak ditemukan variabel Asisten!.. Keluar Proses"
            )
            return
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Memindai Plugin", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Pengimporan Plugin...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Yukki.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Berhasil mengimport: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Selesai mengimport!",
        )
    console.print(
        "[bold green]Selamat!! Ndi Music Bot Berhasil Dimulai!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>Selamat!! Music Bot Berhasil Dimulai!</b>",
        )
    except Exception as e:
        print(
            "\nBot gagal mengakses Group log. Pastikan Anda telah menambahkan bot Anda ke Group log Anda dan dipromosikan sebagai admin!"
        )
        console.print(f"\n[red]Bot Berhenti")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promosikan Bot sebagai Admin di Group LOG")
        console.print(f"\n[red]Bot Berhenti")
        return
    console.print(f"\n┌[red] Bot Dimulai {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_GROUP_ID,
                "<b>Selamat!! Akun Asisten Berhasil Dimulai!</b>",
            )
        except Exception as e:
            print(
                "\nAkun Asisten gagal mengakses Log Group. Pastikan akun asisten dimasukkan Log Group, dan jadikan admin!"
            )
            console.print(f"\n[red]Bot Berhenti")
            return
        try:
            await ASS_CLI_1.join_chat("chFZsokin")
            await ASS_CLI_1.join_chat("friendzonesokin")
        except:
            pass
        console.print(f"├[red] Asisten Berhasil Dimulai {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>Selamat!! Akun Asisten 2 Berhasil Dimulai!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("chFZsokin")
            await ASS_CLI_2.join_chat("friendzonesokin")
        except:
            pass
        console.print(f"├[red] Assistant 2 Started as {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("chFZsokin")
            await ASS_CLI_3.join_chat("friendzonesokin")
        except:
            pass
        console.print(f"├[red] Assistant 3 Started as {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("chFZsokin")
            await ASS_CLI_4.join_chat("friendzonesokin")
        except:
            pass
        console.print(f"├[red] Assistant 4 Started as {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 5 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 5 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_5.join_chat("chFZsokin")
            await ASS_CLI_5.join_chat("friendzonesokin")
        except:
            pass
        console.print(f"├[red] Assistant 5 Started as {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                LOG_GROUP_ID,
                "<b>Selamat!! Log Klien Berhasil Dimulai!</b>",
            )
        except Exception as e:
            print(
                "\nLog Klien gagal mengakses Log Group. Pastikan Log Klien dimasukkan Log Group, dan jadikan admin!"
            )
            console.print(f"\n[red]Bot Berhenti")
            return
        try:
            await LOG_CLIENT.join_chat("chFZsokin")
            await LOG_CLIENT.join_chat("friendzonesokin")
        except:
            pass
    console.print(f"└[red] Ndi Music Bot Memulai Ulang Selesai.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Bot Berhenti")

home_text_pm = f"""✨ **Hello, Selamat Datang!**

🤖{BOT_NAME} **Adalah Bot musik telegram untuk memutar musik+video di obrolan suara Telegram**! Contoh :

╭┉┉┅┅┄┄┄┄•◦ೋ•◦❥•◦ೋ
⧱ Musiqi çalın.
⧱ Videolar oynatın.
⧱ Mahnı endirin.
⧱ Video endirin.
⧱ Daxili ilə YOUTUBE Linkini axtarın.
 •◦ೋ•◦❥•◦ೋ•┈┄┄┄┄┅┅┉╯


💡Temukan semua command bot musik di menu » Menu Perintah«!"""


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "👑 <u> **ᴏᴡɴᴇʀs:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}⌬ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = (
                            user.first_name
                            if not user.mention
                            else user.mention
                        )
                        if smex == 0:
                            smex += 1
                            text += "\n👨‍🚀 <u> **sᴜᴅᴏ ᴜsᴇʀs:**</u>\n"
                        sex += 1
                        text += f"{sex}⌬ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("Tidak ada Pengguna Sudo")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} has Cukup memulai bot untuk memeriksa <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 Mencari Informasi!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Informasi Trek Video**__

🎸**Judul:** {title}

⏳**Durasi:** {duration} Menit
👀**Melihat:** `{views}`
⏰**Waktu Publikasi:** {published}
🎥**Nama Channel:** {channel}
📎**Link Channel:** [Lihat Disini]({channellink})
🔗**Link Video:** [Link]({link})

💫__Pencarian Dipersembahkan oleh {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Menonton Video YouTube", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="✖️ Tutup", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} Cukup memulai bot untuk memeriksa <code>INFORMASI VIDEO</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
            return
    out = private_panel()
    if START_IMG_URL is None:
        await message.reply_text(
            home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
    else:
        await message.reply_photo(
            photo=START_IMG_URL,
            caption=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
    if await is_on_off(5):
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
        return await LOG_CLIENT.send_message(
            LOG_GROUP_ID,
            f"{message.from_user.mention} Bot dimulai.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
        )
    return


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """Hello {first_name},

Tekan tombol dibawah untuk informasi lainnya.

Untuk semua Perintah gunakan: /
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex("search_helper_mess"))
async def search_helper_mess(_, CallbackQuery):
    await CallbackQuery.message.delete()
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await app.send_message(
        CallbackQuery.message.chat.id, text, reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""Hello {query.from_user.first_name},

Tekan tombol dibawah untuk informasi lainnya.

Untuk semua Perintah gunakan: /
 """
    if mod_match:
        module = mod_match.group(1)
        if str(module) == "sudousers":
            userid = query.from_user.id
            if userid in SUDOERS:
                pass
            else:
                return await query.answer(
                    "Tombol ini hanya bisa diakses oleh PENGGUNA SUDO",
                    show_alert=True,
                )
        text = (
            "{} **{}**:\n".format(
                "Disini untuk Bantuan", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ Kembali", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="✖️ Tutup", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
