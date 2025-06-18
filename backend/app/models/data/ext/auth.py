#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std
from ..__variants__.ext import auth as base

from gel.models.pydantic import (
    AnnotatedExpr,
    FuncCall,
    MultiLink,
    MultiProperty,
    OptionalLink,
    OptionalProperty,
    RequiredMultiLink,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as builtins
from builtins import dict, list, tuple
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from .. import std as ___std__
    from ..__types__ import HeaderPayloadSignature_Tuple_e_sBBg

    import builtins as ___builtins__
    from builtins import type



#
# type ext::auth::Auditable
#
class Auditable(base.Auditable):
    created_at: std.datetime
    modified_at: std.datetime

#
# type ext::auth::AuthConfig
#
class AuthConfig(base.AuthConfig, cfg.ExtensionConfig):
    app_name: OptionalProperty[std.str, str]
    logo_url: OptionalProperty[std.str, str]
    dark_logo_url: OptionalProperty[std.str, str]
    brand_color: OptionalProperty[std.str, str]
    auth_signing_key: OptionalProperty[std.str, str]
    token_time_to_live: OptionalProperty[std.duration, timedelta]
    allowed_redirect_urls: MultiProperty[std.str, str]
    providers: MultiLink[ProviderConfig]
    ui: OptionalLink[UIConfig]
    webhooks: MultiLink[WebhookConfig]

#
# type ext::auth::ProviderConfig
#
class ProviderConfig(base.ProviderConfig, cfg.ConfigObject):
    name: std.str

#
# type ext::auth::UIConfig
#
class UIConfig(base.UIConfig, cfg.ConfigObject):
    redirect_to: std.str
    redirect_to_on_signup: OptionalProperty[std.str, str]
    flow_type: FlowType
    app_name: OptionalProperty[std.str, str]
    logo_url: OptionalProperty[std.str, str]
    dark_logo_url: OptionalProperty[std.str, str]
    brand_color: OptionalProperty[std.str, str]

#
# type ext::auth::WebhookConfig
#
class WebhookConfig(base.WebhookConfig, cfg.ConfigObject):
    url: std.str
    events: MultiProperty[WebhookEvent, builtins.str]
    signing_secret_key: OptionalProperty[std.str, str]

#
# type ext::auth::Factor
#
class Factor(base.Factor, Auditable):
    identity: LocalIdentity

#
# type ext::auth::Identity
#
class Identity(base.Identity, Auditable):
    issuer: std.str
    subject: std.str

#
# type ext::auth::PKCEChallenge
#
class PKCEChallenge(base.PKCEChallenge, Auditable):
    challenge: std.str
    auth_token: OptionalProperty[std.str, str]
    refresh_token: OptionalProperty[std.str, str]
    id_token: OptionalProperty[std.str, str]
    identity: OptionalLink[Identity]

#
# type ext::auth::WebAuthnAuthenticationChallenge
#
class WebAuthnAuthenticationChallenge(
    base.WebAuthnAuthenticationChallenge,
    Auditable,
):
    challenge: std.bytes
    factors: RequiredMultiLink[WebAuthnFactor]

#
# type ext::auth::WebAuthnRegistrationChallenge
#
class WebAuthnRegistrationChallenge(
    base.WebAuthnRegistrationChallenge,
    Auditable,
):
    challenge: std.bytes
    email: std.str
    user_handle: std.bytes

#
# type ext::auth::EmailPasswordProviderConfig
#
class EmailPasswordProviderConfig(
    base.EmailPasswordProviderConfig,
    ProviderConfig,
):
    name: std.str
    require_verification: std.bool

#
# type ext::auth::MagicLinkProviderConfig
#
class MagicLinkProviderConfig(base.MagicLinkProviderConfig, ProviderConfig):
    name: std.str
    token_time_to_live: std.duration

#
# type ext::auth::OAuthProviderConfig
#
class OAuthProviderConfig(base.OAuthProviderConfig, ProviderConfig):
    name: std.str
    secret: std.str
    client_id: std.str
    display_name: std.str
    additional_scope: OptionalProperty[std.str, str]

#
# type ext::auth::WebAuthnProviderConfig
#
class WebAuthnProviderConfig(base.WebAuthnProviderConfig, ProviderConfig):
    name: std.str
    relying_party_origin: std.str
    require_verification: std.bool

#
# type ext::auth::EmailFactor
#
class EmailFactor(base.EmailFactor, Factor):
    email: std.str
    verified_at: OptionalProperty[std.datetime, datetime]

#
# type ext::auth::LocalIdentity
#
class LocalIdentity(base.LocalIdentity, Identity):
    subject: std.str

#
# type ext::auth::AppleOAuthProvider
#
class AppleOAuthProvider(base.AppleOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::AzureOAuthProvider
#
class AzureOAuthProvider(base.AzureOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::DiscordOAuthProvider
#
class DiscordOAuthProvider(base.DiscordOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::GitHubOAuthProvider
#
class GitHubOAuthProvider(base.GitHubOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::GoogleOAuthProvider
#
class GoogleOAuthProvider(base.GoogleOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::OpenIDConnectProvider
#
class OpenIDConnectProvider(base.OpenIDConnectProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str
    issuer_url: std.str
    logo_url: OptionalProperty[std.str, str]

#
# type ext::auth::SlackOAuthProvider
#
class SlackOAuthProvider(base.SlackOAuthProvider, OAuthProviderConfig):
    name: std.str
    display_name: std.str

#
# type ext::auth::EmailPasswordFactor
#
class EmailPasswordFactor(base.EmailPasswordFactor, EmailFactor):
    email: std.str
    password_hash: std.str

#
# type ext::auth::MagicLinkFactor
#
class MagicLinkFactor(base.MagicLinkFactor, EmailFactor):
    email: std.str

#
# type ext::auth::WebAuthnFactor
#
class WebAuthnFactor(base.WebAuthnFactor, EmailFactor):
    user_handle: std.bytes
    credential_id: std.bytes
    public_key: std.bytes
def webhook_signing_key_exists(
    webhook_config: type[WebhookConfig],
) -> type[___std__.bool]:
    args: list[Any] = [webhook_config]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.bool,
        FuncCall(
            fname="ext::auth::webhook_signing_key_exists",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def signing_key_exists() -> type[___std__.bool]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.bool,
        FuncCall(
            fname="ext::auth::signing_key_exists",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def _jwt_check_signature(
    jwt: type[HeaderPayloadSignature_Tuple_e_sBBg] | tuple[___builtins__.str, ___builtins__.str, ___builtins__.str],
    key: type[___std__.str] | ___builtins__.str,
    algo: type[JWTAlgo] | builtins.str | UnspecifiedType = Unspecified,
) -> type[___std__.json]:
    args: list[Any] = [jwt, key, algo]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.json,
        FuncCall(
            fname="ext::auth::_jwt_check_signature",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

def _jwt_parse(
    token: type[___std__.str] | ___builtins__.str,
) -> type[HeaderPayloadSignature_Tuple_e_sBBg]:
    args: list[Any] = [token]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        __types__.HeaderPayloadSignature_Tuple_e_sBBg,
        FuncCall(
            fname="ext::auth::_jwt_parse",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<header:std::str, payload:std::str, signature:std::str>'),
        )
    )

def _jwt_verify(
    token: type[___std__.str] | ___builtins__.str,
    key: type[___std__.str] | ___builtins__.str,
    algo: type[JWTAlgo] | builtins.str | UnspecifiedType = Unspecified,
) -> type[___std__.json]:
    args: list[Any] = [token, key, algo]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.json,
        FuncCall(
            fname="ext::auth::_jwt_verify",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )



from .. import __types__  # noqa: E402 F403
from ..__variants__.ext.auth import FlowType, JWTAlgo, WebhookEvent  # noqa: E402 F403

from builtins import bool, bytes, str  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403


__all__ = (
    'AppleOAuthProvider',
    'Auditable',
    'AuthConfig',
    'AzureOAuthProvider',
    'DiscordOAuthProvider',
    'EmailFactor',
    'EmailPasswordFactor',
    'EmailPasswordProviderConfig',
    'Factor',
    'FlowType',
    'GitHubOAuthProvider',
    'GoogleOAuthProvider',
    'Identity',
    'JWTAlgo',
    'LocalIdentity',
    'MagicLinkFactor',
    'MagicLinkProviderConfig',
    'OAuthProviderConfig',
    'OpenIDConnectProvider',
    'PKCEChallenge',
    'ProviderConfig',
    'SlackOAuthProvider',
    'UIConfig',
    'WebAuthnAuthenticationChallenge',
    'WebAuthnFactor',
    'WebAuthnProviderConfig',
    'WebAuthnRegistrationChallenge',
    'WebhookConfig',
    'WebhookEvent',
)
