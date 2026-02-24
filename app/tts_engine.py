import pyttsx3
import uuid
import os


class EmpathyVoiceEngine:

    def configure_voice(self, engine, emotion, intensity):
        base_rate = 170
        base_volume = 0.9

        if emotion == "excited":
            rate = base_rate + int(intensity * 80)
            volume = 1.0

        elif emotion == "happy":
            rate = base_rate + int(intensity * 50)
            volume = 1.0

        elif emotion == "angry":
            rate = base_rate + int(abs(intensity) * 30)
            volume = 1.0

        elif emotion == "concerned":
            rate = base_rate - int(abs(intensity) * 40)
            volume = 0.7

        else:
            rate = base_rate
            volume = base_volume

        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)

    def save_audio(self, text, emotion, intensity):

        if not os.path.exists("static"):
            os.makedirs("static")

        unique_filename = f"static/output_{uuid.uuid4().hex}.wav"

        # 🔥 Create NEW engine every request
        engine = pyttsx3.init("sapi5")

        self.configure_voice(engine, emotion, intensity)

        engine.save_to_file(text, unique_filename)
        engine.runAndWait()
        engine.stop()

        return unique_filename