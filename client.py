class SpeechFillerWordRemoverCleanerClient:
    def detect_and_clean_fillers(self, transcript_segments=[{'word': 'Um', 'start_sec': 1.2, 'end_sec': 1.6}, {'word': 'hello', 'start_sec': 1.8, 'end_sec': 2.1}, {'word': 'like', 'start_sec': 4.5, 'end_sec': 4.8}]):
        fillers_set = {'um', 'uh', 'like', 'you know', 'ah'}
        flagged_fillers = [seg for seg in transcript_segments if seg.get('word', '').lower() in fillers_set]
        return {
            'cleaner_run_id': 'flr_cln_3301',
            'total_words_evaluated': len(transcript_segments),
            'fillers_detected_count': len(flagged_fillers),
            'total_filler_duration_sec': round(sum(f['end_sec'] - f['start_sec'] for f in flagged_fillers), 2),
            'flagged_words': [f['word'] for f in flagged_fillers],
            'crossfade_smoothing_duration_ms': 25,
            'clean_cutlist_export_url': 'https://media.audio.genpark.ai/cutlists/flr_cln_3301.json'
        }
