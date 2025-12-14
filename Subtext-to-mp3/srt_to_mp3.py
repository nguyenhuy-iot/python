import pysrt
from gtts import gTTS
from pydub import AudioSegment

subs = pysrt.open("subtitle_vi.srt", encoding="utf-8")

final_audio = AudioSegment.silent(duration=0)

for i, sub in enumerate(subs):
    start_ms = sub.start.ordinal
    end_ms = sub.end.ordinal
    duration = end_ms - start_ms

    tts = gTTS(text=sub.text, lang="vi")
    temp_file = f"temp_{i}.mp3"
    tts.save(temp_file)

    voice = AudioSegment.from_mp3(temp_file)

    # Trim or adjust duration if needed
    if len(voice) > duration:
        voice = voice[:duration]

    if len(final_audio) < start_ms:
        final_audio += AudioSegment.silent(start_ms - len(final_audio))

    final_audio += voice

final_audio.export("voice_vi.mp3", format="mp3")

print("DONE: voice_vi.mp3")
