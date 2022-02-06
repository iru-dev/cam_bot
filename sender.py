#!/bin/python3
import logging
import telebot
import config
import sys

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.
bot = telebot.TeleBot(config.TG_TOKEN, threaded=True)

video = open(sys.argv[1], 'rb')
bot.send_video(config.ADMIN[0], video, caption='Обнаружено движение')
