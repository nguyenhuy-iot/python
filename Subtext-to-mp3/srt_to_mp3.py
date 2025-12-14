import pysrt
from gtts import gTTS
from pydub import AudioSegment

def speed_up_audio(sound, speed):
    return sound._spawn(
        sound.raw_data,
        overrides={
            "frame_rate": int(sound.frame_rate * speed)
        }
    ).set_frame_rate(sound.frame_rate)

subs = pysrt.open("subtitle_vi.srt", encoding="utf-8")

final_audio = AudioSegment.silent(duration=0)

MAX_SPEED = 1.4  # limit the speed to avoid audio distortion

for i, sub in enumerate(subs):
    start_ms = sub.start.ordinal
    end_ms = sub.end.ordinal
    duration = end_ms - start_ms

    tts = gTTS(text=sub.text, lang="vi")
    temp_file = f"temp_{i}.mp3"
    tts.save(temp_file)

    voice = AudioSegment.from_mp3(temp_file)
    voice = speed_up_audio(voice, MAX_SPEED)

    voice_len = len(voice)
    if voice_len > duration:
        speed = voice_len / duration
        print(f"[{i}] voice_len={voice_len} ms | duration={duration} ms | speed={speed:.2f}")
        voice = voice[:duration]

    # Chèn im lặng để khớp thời gian bắt đầu subtitle
    if len(final_audio) < start_ms:
        final_audio += AudioSegment.silent(start_ms - len(final_audio))

    final_audio += voice

final_audio.export("voice_vi.mp3", format="mp3")

print("DONE: voice_vi.mp3")
