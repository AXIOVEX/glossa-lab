"""World Language Graph schema vocabularies (Spec 108, design sections 1-2).

The schema enforces the design's separations mechanically:
languages and scripts are distinct node kinds; placement is
never a node field; the seven historical predicates are
distinct from the structural relations; status scales are
kind-bound.
"""

SCHEMA_VERSION = "wlg-1.0"

NODE_KINDS = {"LANGUAGE", "SCRIPT", "CONTEXT"}
LANGUAGE_SUBTYPES = {
    "ATTESTED", "RECONSTRUCTED", "INFERRED_UNKNOWN",
    "FAMILY_OR_CLADE", "DOCUMENTATION_UNIT",
}
SCRIPT_SUBTYPES = {
    "ATTESTED", "RECONSTRUCTED", "INFERRED_UNKNOWN", "SIGN_LIST_UNIT",
}
CONTEXT_SUBTYPES = {
    "POPULATION_OR_COMMUNITY", "REGION", "SITE", "POLITY",
    "ARCHAEOLOGICAL_CULTURE", "RELIGIOUS_TRADITION",
}
SCRIPT_STATUS = {"S0", "S1", "S2", "S3", "S4"}
LANGUAGE_STATUS = {"L0", "L1", "L2", "L3", "L4", "L5"}

NODE_REQUIRED = [
    "node_id", "kind", "subtype", "label", "status_code",
    "coverage_depth", "placement_state", "geometry_type",
    "covariates_state",
]
# The placement rule (design 5.7): a node record may never
# carry any of these keys. Placement lives in assertions
# and PROPOSED_RELATION edges only.
FORBIDDEN_NODE_FIELDS = {"family", "language_family", "family_id", "placement"}

HISTORICAL_PREDICATES = {
    "GENETIC_DESCENT", "CONTACT_BORROWING", "SCRIPT_DESCENT",
    "SCRIPT_BORROWING", "AREAL_CONVERGENCE", "POPULATION_MOVEMENT",
    "PROPOSED_RELATION",
}
STRUCTURAL_PREDICATES = {"WRITES", "ATTESTED_AT", "ADMINISTERED_BY", "USED_IN_POLITY"}
ALL_PREDICATES = HISTORICAL_PREDICATES | STRUCTURAL_PREDICATES

EDGE_REQUIRED = [
    "edge_id", "predicate", "subject_id", "object_id",
    "evidence_class", "confidence_label", "source_refs",
    "asserted_by", "basis", "temporal_scope", "feature_scope",
    "falsifier_or_removal_condition", "status", "review_state",
]
ASSERTION_REQUIRED = [
    "assertion_id", "subject_id", "field", "value",
    "evidence_class", "confidence_label", "source_refs",
    "source_grade", "review_state", "asserted_by", "removal_condition",
]
EVIDENCE_CLASSES = {"F", "K", "H"}
CONFIDENCE_LABELS = {"SECURE", "WELL_SUPPORTED", "PROBABLE", "POSSIBLE", "SPECULATIVE"}
SOURCE_GRADES = {"P1", "P2", "P3", "P4"}
REVIEW_STATES = {"UNREVIEWED", "SOURCE_CHECKED", "INDEPENDENTLY_CHECKED", "ADJUDICATED"}
COVERAGE_DEPTHS = {"SKELETON", "STANDARD", "DOSSIER"}
GEOMETRY_TYPES = {
    "ATTESTED_FINDSPOT_SET", "ATTESTED_DISTRIBUTION", "DISPLAY_CENTROID",
    "INFERRED_HOMELAND", "RECONSTRUCTED_STAGE_AREA", "CONTACT_ZONE",
    "NO_GEOMETRY",
}
GAP_KINDS = {
    "SCRIPT_UNDECIPHERED", "LANGUAGE_NOT_UNDERSTOOD",
    "SCRIPT_AND_LANGUAGE", "CLASSIFICATION_UNRESOLVED",
    "ATTESTATION_ONLY", "LINGUISTIC_STATUS_DISPUTED",
}
BLOCKER_TYPES = {"INFORMATION", "ACCESS", "POWER", "PERMISSION", "EXPERTISE"}
EVIDENCE_BANDS = {"A", "B", "C", "D"}
