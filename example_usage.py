from client import SpeechFillerWordRemoverCleanerClient

def main():
    client = SpeechFillerWordRemoverCleanerClient()
    res = client.detect_and_clean_fillers()
    print('Speech Filler Cleaner: ' + res['cleaner_run_id'] + ' (Fillers: ' + str(res['fillers_detected_count']) + ')')
    print('Duration Saved: ' + str(res['total_filler_duration_sec']) + 's | Flagged: ' + str(res['flagged_words']))
    print('Cutlist URL: ' + res['clean_cutlist_export_url'])

if __name__ == '__main__':
    main()
