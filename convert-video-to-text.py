import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

num_seconds_video= 52*60
print("The video is {} seconds".format(num_seconds_video))
l=list(range(0,num_seconds_video+1,60))

diz={}
for i in range(len(l)-1):
    #Makes a new video file playing video file filename between the times t1 and t2
    ffmpeg_extract_subclip("videorl.mp4", l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
    
    #A video clip originating from a movie file
    clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i+1))

    #Writes an audio file from the AudioClip.
    clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
    #Creates a new Recognizer instance, which represents a collection of speech recognition settings and functionality
    r = sr.Recognizer()
    #Creates a new AudioFile instance given a WAV/AIFF/FLAC audio file filename_or_fileobject. Subclass of AudioSource
    audio = sr.AudioFile("converted/converted{}.wav".format(i+1))

    with audio as source:
        #Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise. 
        # Intended to calibrate the energy threshold with the ambient energy level. 
        # Should be used on periods of audio without speech - will stop early if any speech is detected
      r.adjust_for_ambient_noise(source)
      #Records up to duration seconds of audio from source starting at offset into an AudioData instance, which it returns
      audio_file = r.record(source)
    #Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API
    result = r.recognize_google(audio_file)
    diz['chunk{}'.format(i+1)]=result