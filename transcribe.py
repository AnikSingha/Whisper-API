import whisper
import pysrt


# call whisper AI to transcribe file
def transcribe(file_name, model):
    result = model.transcribe(file_name, fp16=False)
    return result # dictionary with 3 keys: text, segments, language

def buildSRT(result):
    subs = pysrt.SubRipFile()
    subIndex = 1 # index used in srt fle

    for i in range(len(result["segments"])): # iterate through segments to build srt
        segment_start = result["segments"][i]["start"]
        segment_end = result["segments"][i]["end"]
        text = result["segments"][i]["text"]

        if segment_start >= 0 and segment_end <= 30: # only generate subtitles for the first 30 seconds
            sub = pysrt.SubRipItem(index=subIndex,
                                start=pysrt.SubRipTime(seconds=segment_start),
                                end=pysrt.SubRipTime(seconds=segment_end),
                                text=text)
            subs.append(sub)
            subIndex += 1

    return subs

def createSRTFile(file_name, model, outName = "output.srt",):
    result = transcribe(file_name, model)
    subs = buildSRT(result)
    subs.save(outName)
