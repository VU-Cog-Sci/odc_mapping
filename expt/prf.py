import argparse
from session import PRFSession

def main(subject, run, reset):
    session = PRFSession(subject_initials=subject,
                         index_number=run,
                         reset_positions=reset,
                         simulate_mri_trigger=True)
    session.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject",
                        #nargs='?',
                        type=str,
                        help="Subject experiment")
    parser.add_argument("run",
                        type=str,
                        default='*',
                        help="Run experiment")
    parser.add_argument("-r",
                        "--reset",
                        action='store_true',
                        help="Whether to reset positiong parameters to default.")
    args = parser.parse_args()
    main(subject=args.subject,
         run=args.run,
         reset=args.reset)
