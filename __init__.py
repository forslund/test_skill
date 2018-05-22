# -*- coding: utf-8 -*-
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from adapt.intent import IntentBuilder
from datetime import datetime, timedelta

class TestSkill(MycroftSkill):
    @intent_handler(IntentBuilder('TestIntent').require('GoodBye'))
    def test_handler(self, message):
        LOG.info('Good bye!')


def create_skill():
    return TestSkill()
