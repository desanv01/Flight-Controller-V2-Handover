"""Check the offline comparator's input and numerical semantics."""
from decimal import Decimal
import unittest
from compare_parameters import compare, parse_text, review_group


class ParameterComparisonTests(unittest.TestCase):
    def test_equivalent_numeric_forms_and_bom_comments(self):
        baseline = parse_text('\ufeff# comment\nRC_OPTIONS,8224\nMOT_SPIN_ARM,0.10\n')
        current = parse_text('; comment\nRC_OPTIONS 8.224e3\nMOT_SPIN_ARM 0.1\n')
        self.assertEqual(compare(baseline, current), [])

    def test_changes_additions_and_missing_entries(self):
        baseline = parse_text('RC6_OPTION,153\nOLD_PARAM,1\nUNCHANGED,0\n')
        current = parse_text('RC6_OPTION,0\nNEW_PARAM,2\nUNCHANGED,0.0\n')
        rows = compare(baseline, current)
        self.assertEqual([(r['parameter'], r['status']) for r in rows],
                         [('NEW_PARAM', 'added'), ('OLD_PARAM', 'missing'), ('RC6_OPTION', 'changed')])
        self.assertEqual(rows[-1]['baseline_value'], '153')
        self.assertEqual(rows[-1]['current_value'], '0')

    def test_duplicates_and_invalid_values_are_rejected(self):
        for text in ['RC_OPTIONS,32\nRC_OPTIONS,8224', 'RC_OPTIONS,NaN', 'RC_OPTIONS,Infinity',
                     'RC_OPTIONS,unknown', 'RC_OPTIONS,1,2', '# empty']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_text(text)

    def test_review_groups_do_not_turn_counters_into_acceptance(self):
        self.assertIn('not flight evidence', review_group('STAT_FLTCNT'))
        self.assertIn('do not copy', review_group('RC3_TRIM'))
        self.assertIn('startup', review_group('INS_GYROFFS_X'))

    def test_historical_final_transition_preserves_originals(self):
        from compare_parameters import ROOT, DEFAULT_BASELINE
        other = ROOT / 'config/historical-fc2-snapshots/FC2_radio_corrected_2026-10-21.param'
        before, final = other.read_bytes(), DEFAULT_BASELINE.read_bytes()
        rows = compare(parse_text(before.decode()), parse_text(final.decode()))
        rc6 = next(row for row in rows if row['parameter'] == 'RC6_OPTION')
        self.assertEqual((Decimal(rc6['baseline_value']), Decimal(rc6['current_value'])), (153, 0))
        self.assertEqual(other.read_bytes(), before)
        self.assertEqual(DEFAULT_BASELINE.read_bytes(), final)


if __name__ == '__main__':
    unittest.main()
