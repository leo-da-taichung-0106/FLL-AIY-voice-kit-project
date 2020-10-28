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
    audio_no=1
    with aiy.audio.get_recorder():
        while True:



            #aiy.voicehat.get_status_ui().set_trigger_sound_wave('/opt/aiy/projects-python/src/examples/voice/appler.wav')
            wavefile = '/opt/aiy/projects-python/src/examples/voice/alsa/Front_Center.wav'
            wavefileapplert = '/opt/aiy/projects-python/src/examples/voice/applert.wav'
            wavefile1 = '/opt/aiy/projects-python/src/examples/voice/audio_files/ha1.wav'
            wavefile2 = '/opt/aiy/projects-python/src/examples/voice/audio_files/ha2.wav'
            wavefile3 = '/opt/aiy/projects-python/src/examples/voice/audio_files/ha3.wav'
            wavefile4 = '/opt/aiy/projects-python/src/examples/voice/audio_files/ha4.wav'
            wavefile5 = '/opt/aiy/projects-python/src/examples/voice/audio_files/1.wav'
            wavefile6 = '/opt/aiy/projects-python/src/examples/voice/audio_files/2.wav'
            wavefile7 = '/opt/aiy/projects-python/src/examples/voice/audio_files/3.wav'
            wavefile8 = '/opt/aiy/projects-python/src/examples/voice/audio_files/4.wav'
            waveerr = '/opt/aiy/projects-python/src/examples/voice/e.wav'

            #expanded_path = os.path.expanduser(wavefile)
            #if os.path.exists(expanded_path):
            #    self._trigger_sound_wave = expanded_path



            if audio_no==1:
                aiy.audio.play_wave(wavefileapplert)
                aiy.audio.play_wave(wavefile1)
            if audio_no==2:
                aiy.audio.play_wave(wavefile2)
            if audio_no==3:
                aiy.audio.play_wave(wavefile2)

            print('Press the button .....')
            button.wait_for_press()

            status_ui.status('ready')
            status_ui.status('press')
            print('Listening...')
            text, audio = assistant.recognize()
            if text:
                if text == 'hi' :
                    print('Hi!')
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                if text == 'yes':
                    print('yes')
                elif text == 'no':
                    print('no')
                else:
                    aiy.audio.play_wave(waveerr)
                print('You said "', text, '"')

            audio_no= audio_no +1
            # if audio:
            #     aiy.audio.play_audio(audio)


if __name__ == '__main__':
    main()
