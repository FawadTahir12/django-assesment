class ReportGenerator:
    
    def generate_report(self, analysis_results):  # Generate reposrt of images after analysis
        report_text = "Image Analysis Report\n" + "-" * 50 + "\n"

        for result in analysis_results:
            report_text += f"""
            Image URL: {result['image_url']}
            Edge Count: {result['edge_count']}
            Status: {result['status']}
            """ + "-" * 50 + "\n"

        return report_text
