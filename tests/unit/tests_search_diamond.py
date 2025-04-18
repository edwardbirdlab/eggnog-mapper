##
## CPCantalapiedra 2020

import shutil, os, unittest
from argparse import Namespace

from eggnogmapper.common import DIAMOND, ITYPE_CDS, ITYPE_PROTS
from eggnogmapper.search.diamond.diamond import DiamondSearcher, SENSMODE_MORE_SENSITIVE, \
    ALLOW_OVERLAPS_NONE

class Test(unittest.TestCase):
    
    def setUp(self):
        os.mkdir("tests/unit/out/")

    def tearDown(self):
        if os.path.exists("tests/unit/out"):
            shutil.rmtree("tests/unit/out")
            
    # Tests
    def test_run_diamond_blastp(self):
        args = Namespace(itype=ITYPE_PROTS,
                         translate=False,
                         trans_table=None,
                         allow_overlaps=ALLOW_OVERLAPS_NONE,
                         overlap_tol=0.0,
                         dmnd_db="tests/fixtures/eggnog_proteins.dmnd",
                         cpu=2,
                         sensmode=SENSMODE_MORE_SENSITIVE,
                         dmnd_iterate=False,
                         dmnd_ignore_warnings=False,
                         dmnd_algo=None,
                         query_cover=0,
                         subject_cover=0,
                         matrix=None,
                         dmnd_frameshift=None,
                         gapopen=None,
                         gapextend=None,
                         dmnd_block_size=None,
                         dmnd_index_chunks=None,
                         pident=0,
                         dmnd_evalue=0.001,
                         dmnd_score=60,
                         outfmt_short=True,
                         temp_dir="tests/unit/out/",
                         no_file_comments=None,
                         resume=False,
                         decorate_gff_ID_field=None)
        
        fasta_file = "tests/fixtures/test_queries.fa"
        output_file = "tests/unit/out/test_run_diamond_blastp.seed_orthologs"
                
        searcher = DiamondSearcher(args, "tests/fixtures/eggnog_proteins.dmnd")
        cmd = searcher.run_diamond(fasta_file, output_file)[0]
        
        self.assertIsNotNone(cmd)
        self.assertTrue(cmd.startswith(DIAMOND))

        searcher.clear()
        
        return

    def test_run_diamond_blastx(self):
        args = Namespace(itype=ITYPE_CDS,
                         translate=False,
                         trans_table=None,
                         allow_overlaps=ALLOW_OVERLAPS_NONE,
                         overlap_tol=0.0,
                         dmnd_db="tests/fixtures/eggnog_proteins.dmnd",
                         cpu=2,
                         sensmode=SENSMODE_MORE_SENSITIVE,
                         dmnd_iterate=False,
                         dmnd_ignore_warnings=False,
                         dmnd_algo=None,
                         query_cover=0,
                         subject_cover=0,
                         matrix=None,
                         dmnd_frameshift=None,
                         gapopen=None,
                         gapextend=None,
                         dmnd_block_size=None,
                         dmnd_index_chunks=None,
                         pident=0,
                         dmnd_evalue=0.001,
                         dmnd_score=60,
                         outfmt_short=True,
                         temp_dir="tests/unit/out/",
                         no_file_comments=None,
                         resume=False,
                         decorate_gff_ID_field=None)
        
        fasta_file = "tests/fixtures/test_queries.fna"
        output_file = "tests/unit/out/test_run_diamond_blastx.seed_orthologs"
                
        searcher = DiamondSearcher(args, "tests/fixtures/eggnog_proteins.dmnd")
        
        cmd = searcher.run_diamond(fasta_file, output_file)[0]
        
        self.assertIsNotNone(cmd)
        self.assertTrue(cmd.startswith(DIAMOND))

        searcher.clear()
        
        return

    def test_parse_diamond(self):
        args = Namespace(itype=ITYPE_PROTS,
                         translate=False,
                         trans_table=None,
                         allow_overlaps=ALLOW_OVERLAPS_NONE,
                         overlap_tol=0.0,
                         dmnd_db="tests/fixtures/eggnog_proteins.dmnd",
                         cpu=2,
                         sensmode=SENSMODE_MORE_SENSITIVE,
                         dmnd_iterate=False,
                         dmnd_ignore_warnings=False,
                         dmnd_algo=None,
                         query_cover=0,
                         subject_cover=0,
                         matrix=None,
                         dmnd_frameshift=None,
                         gapopen=None,
                         gapextend=None,
                         dmnd_block_size=None,
                         dmnd_index_chunks=None,
                         pident=0,
                         dmnd_evalue=0.001,
                         dmnd_score=60,
                         outfmt_short=True,
                         temp_dir="tests/unit/out/",
                         no_file_comments=None,
                         resume=False,
                         decorate_gff_ID_field=None)
        
        searcher = DiamondSearcher(args, "tests/fixtures/eggnog_proteins.dmnd")
        
        seed_orthologs_file = "tests/fixtures/test_diamond_blastp.out"
        parsed = searcher._parse_diamond(seed_orthologs_file)

        # convert generator to list and
        # remove the boolean of --resume mode
        parsed = [x for x in parsed]
        
        expected = [['1000565.METUNv1_03812', '1000565.METUNv1_03812', 1.9e-207, 716.8],
                    ['362663.ECP_0061', '362663.ECP_0061', 0.0, 1636.3]]
        
        self.assertEqual(parsed, expected)

        searcher.clear()
        
        return
    
if __name__ == '__main__':
    
    unittest.main()

## END
