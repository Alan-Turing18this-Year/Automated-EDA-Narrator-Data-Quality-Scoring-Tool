# Composition + dunder method
from loader import DataLoader
from preprocessor import Preprocessor
from eda_analyzer import NumericAnalyzer, CategoricalAnalyzer
from quality_scorer import QualityScorer
from narrator import Narrator
from report_builder import ReportBuilder

class DatasetPipeline:
    def __init__(self, path):
        self.loader = DataLoader(path)       # composition
        self.preprocessor = None
        self.analyzer = None
        self.eda_results = None
        self.scores = None
        self.narrative = None
        self.report = None

    def run(self):
        df = self.loader.load()
        self.preprocessor = Preprocessor(df).trim_strings(df.select_dtypes(include='object').columns.tolist())
        df_clean = self.preprocessor.get_df()

        # Numeric + categorical analysis (inheritance + polymorphism)
        num_analyzer = NumericAnalyzer(df_clean)
        cat_analyzer = CategoricalAnalyzer(df_clean)
        self.eda_results = {**num_analyzer.run_all(), **cat_analyzer.run_all()}

        # scoring
        scorer = QualityScorer(self.eda_results, df_len=len(df_clean))
        scorer.overall_score()
        self.scores = scorer.scores

        # narration
        narrator = Narrator(self.eda_results, self.scores)
        self.narrative = narrator.generate()

        # report
        builder = ReportBuilder(self.narrative, self.scores, self.eda_results)
        self.report = builder.to_markdown()
        return self.report

    # dunder method
    def __repr__(self):
        return f"<DatasetPipeline loader={repr(self.loader)}>"
