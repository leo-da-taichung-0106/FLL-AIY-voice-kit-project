#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import logging
import os.path

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button .....')
            button.wait_for_press()
            print("Hi")
            leo=aiy.voicehat.get_led()
            #leo.set_state(aiy.voicehat.LED.BLINK)
            leo.set_state(aiy.voicehat.LED.ON)
            print("haha")
            leo.start()
            #aiy.voicehat.get_status_ui().set_trigger_sound_wave('/opt/aiy/projects-python/src/examples/voice/appler.wav')
            wavefile = '/opt/aiy/projects-python/src/examples/voice/alsa/Front_Center.wav'

            #wavefile = '/opt/aiy/projects-python/src/examples/voice/applert.wav'
            wavefile = '/opt/aiy/projects-python/src/examples/voice/Thanos.wav'
            #wavefile = '/opt/aiy/projects-python/src/examples/voice/Click.wav'

	         #expanded_path = os.path.expanduser(wavefile)
            #if os.path.exists(expanded_path):
            #    self._trigger_sound_wave = expanded_path




            aiy.audio.play_wave(wavefile)
            aiy.audio.play_wave(wavefile1)
            


            # status_ui.status('press')
            # print('Listening...')
            # text, audio = assistant.recognize()
            # if text:
            #     if text == 'goodbye':
            #         status_ui.status('stopping')
            #         print('Bye!')
            #         break
            #     print('You said "', text, '"')
            # if audio:
            #     aiy.audio.play_audio(audio)


if __name__ == '__main__':
    main()
