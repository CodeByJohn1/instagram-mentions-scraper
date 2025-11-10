thonimport json
import csv
import os
import logging
import pandas as pd

class Exporter:
    @staticmethod
    def export(data, filename, file_format="json"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            if file_format.lower() == "json":
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            elif file_format.lower() == "csv":
                df = pd.DataFrame(data)
                df.to_csv(filename, index=False)
            elif file_format.lower() == "excel":
                df = pd.DataFrame(data)
                df.to_excel(filename, index=False)
            else:
                logging.warning(f"Unsupported export format '{file_format}', defaulting to JSON")
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logging.error(f"Failed to export data: {str(e)}")